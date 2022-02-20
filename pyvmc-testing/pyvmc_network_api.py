import requests                         # need this for Get/Post/Delete
import configparser                     # parsing config file
import operator
import time
import json
import sys
from deepdiff import DeepDiff
from os.path import exists
from prettytable import PrettyTable


if not exists("./config.ini"):
    print('config.ini is missing - rename config.ini.example to config.ini and populate the required values inside the file.')
    sys.exit()

DEBUG_MODE = False

config = configparser.ConfigParser()
config.read("./config.ini")
strProdURL      = config.get("vmcConfig", "strProdURL")
strCSPProdURL   = config.get("vmcConfig", "strCSPProdURL")
Refresh_Token   = config.get("vmcConfig", "refresh_Token")
ORG_ID          = config.get("vmcConfig", "org_id")
SDDC_ID         = config.get("vmcConfig", "sddc_id")

if config.has_section("vtcConfig"):
    aws_acc         = config.get("vtcConfig", "MyAWS")
    region          = config.get("vtcConfig", "AWS_region")
    dxgw_id         = config.get("vtcConfig", "DXGW_id")
    dxgw_owner      = config.get("vtcConfig", "DXGW_owner")
else:
    print('config.ini is outdated - the vtcConfig section is missing. Please insert the vtcConfig section in config.ini.example into your config.ini file. All transit gateway commands will fail without this configuration change.')

if config.has_section("tkgConfig"):
    egress_CIDR     = config.get("tkgConfig", "egress_CIDR")
    ingress_CIDR    = config.get("tkgConfig", "ingress_CIDR")
    namespace_CIDR  = config.get("tkgConfig", "namespace_CIDR")
    service_CIDR    = config.get("tkgConfig", "service_CIDR")
else:
    print('config.ini is outdated - the tkgConfig section is missing. Please insert the tkgConfig section in config.ini.example into your config.ini file. All TKG commands will fail without this configuration change.')

if len(strProdURL) == 0 or len(strCSPProdURL) == 0 or len(Refresh_Token) == 0 or len(ORG_ID) == 0 or len(SDDC_ID) == 0:
    print('strProdURL, strCSPProdURL, Refresh_Token, ORG_ID, and SDDC_ID must all be populated in config.ini')
    sys.exit()

class data():
    sddc_name       = ""
    sddc_status     = ""
    sddc_region     = ""
    sddc_cluster    = ""
    sddc_hosts      = 0
    sddc_type       = ""


def getNSXTproxy(org_id, sddc_id, sessiontoken):
    """ Gets the Reverse Proxy URL """
    myHeader = {'csp-auth-token': sessiontoken}
    myURL = "{}/vmc/api/orgs/{}/sddcs/{}".format(strProdURL, org_id, sddc_id)
    response = requests.get(myURL, headers=myHeader)
    json_response = response.json()
    proxy_url = json_response['resource_config']['nsx_api_public_endpoint_url']
    return proxy_url

def getSDDCnetworks(proxy_url, sessiontoken):
    """ Gets the SDDC Networks """
    myHeader = {'csp-auth-token': sessiontoken}
    myURL = (proxy_url + "/policy/api/v1/infra/tier-1s/cgw/segments")
    response = requests.get(myURL, headers=myHeader)
    json_response = response.json()
    sddc_networks = json_response['results']
    return sddc_networks

def getSDDCT0routes(proxy_url, session_token):
    myHeader = {'csp-auth-token': session_token}
    myURL = "{}/policy/api/v1/infra/tier-0s/vmc/routing-table?enforcement_point_path=/infra/sites/default/enforcement-points/vmc-enforcementpoint".format(proxy_url)
    response = requests.get(myURL, headers=myHeader)
    json_response = response.json()
    t0_routes = json_response['results'][1]['route_entries']
    return t0_routes

def getSDDCT0PrefixLists(csp_url, session_token):
    myHeader = {'csp-auth-token': session_token}
    myURL = f'{csp_url}/policy/api/v1/infra/tier-0s/vmc/prefix-lists'
    response = requests.get(myURL, headers=myHeader)
    if response.status_code == 200:
        json_response = response.json()
        prefixlists = json_response['results']
        # clear results for any prefix lists found that contain "System created prefix list"
        # this will return empty dictionaries for any containing the above string
        for prefix in prefixlists:
            if prefix['description'].__contains__('System created prefix list'):
                prefix.clear()
        # remove empty dictionaries
        while {} in prefixlists:
            prefixlists.remove({})
        return prefixlists
    else:
        print (f'API call failed with status code {response.status_code}. URL: {myURL}.')