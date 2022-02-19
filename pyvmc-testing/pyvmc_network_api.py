import requests                         # need this for Get/Post/Delete
import configparser                     # parsing config file
import operator
import time
import json
import sys
from deepdiff import DeepDiff
from os.path import exists
from prettytable import PrettyTable

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