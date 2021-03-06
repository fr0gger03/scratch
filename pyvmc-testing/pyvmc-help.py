print("\nAWS Account and VPC")
print("\tset-sddc-connected-services: change whether to use S3 over the Internet or via the ENI")
print("\tshow-compatible-subnets [LINKEDACCOUNTID] [REGION]: show compatible native AWS subnets connected to the SDDC")
print("\tshow-connected-accounts: show native AWS accounts connected to the SDDC")
print("\tshow-sddc-connected-vpc: show the VPC connected to the SDDC")
print("\tshow-shadow-account: show the Shadow AWS Account VMC is deployed in")
print("\nBGP and Networking")
print("\tnew-t0-prefix-list: create a new T0 BGP Prefix List")
print("\tremove-t0-prefix-list [PREFIX LIST ID]: you can see current prefix list with 'show-t0-prefix-lists': remove a T0 BGP Prefix List")
print("\tset-bgp-as [ASN]: update the BGP AS number")
print("\tset-mtu: set the MTU configured over the Direct Connect")
print("\tshow-mtu: show the MTU configured over the Direct Connect")
print("\tshow-egress-interface-counters: show current Internet interface egress counters")
print("\tshow-sddc-bgp-as: show the BGP AS number")
print("\tshow-sddc-bgp-vpn: show whether DX is preferred over VPN")
print("\tshow-t0-bgp-neighbors: show T0 BGP neighbors")
print("\tshow-t0-prefix-lists: show T0 prefix lists")
print("\tshow-t0-routes: show routes at the T0 router")
print("\nDNS ")
print("\tshow-dns-services: show DNS services")
print("\tshow-dns-zones: show DNS zones")
print("\nInventory Groups")
print("\tnew-group [CGW/MGW] [Group_ID]: create a new group")
print("\tremove-group [CGW/MGW][Group_ID]: remove a group")
print("\tshow-group [CGW/MGW] [Group_ID]: show existing groups")
print("\tshow-group-association [CGW/MGW] [Group_ID]: show security rules used by a groups")
print("\nFirewall - Distributed")
print("\tnew-dfw-rule [NAME] [SOURCE-GROUPS] [DESTINATION-GROUPS] [SERVICE] [ACTION] [SECTION] [SEQUENCE-NUMBER]: create a new DFW security rule")
print("\tnew-dfw-section [NAME][CATEGORY]: create a new DFW section")
print("\tremove-dfw-rule [SECTION_ID][RULE_ID]: delete a DFW rule")
print("\tremove-dfw-section [RULE_ID]: delete a DFW section")
print("\tshow-dfw-section: show the DFW sections")
print("\tshow-dfw-section-rules [SECTION]: show the DFW security rules within a section")
print("\nFirewall - T0")
print("\tnew-cgw-rule [NAME] [SOURCE-GROUPS] [DESTINATION-GROUPS] [SERVICE] [ACTION] [SCOPE] [SEQUENCE-NUMBER]: create a new CGW security rule")
print("\tnew-mgw-rule [NAME] [SOURCE-GROUPS] [DESTINATION-GROUPS] [SERVICE] [ACTION] [SEQUENCE-NUMBER]: create a new MGW security rule")
print("\tremove-cgw-rule [RULE_ID]: delete a CGW security rule")
print("\tremove-mgw-rule [RULE_ID]: delete a MGW security rule")
print("\tshow-cgw-rule: show the CGW security rules")
print("\tshow-mgw-rule: show the MGW security rules")
print("\nFirewall Services")
print("\tnew-service: create a new service")
print("\tremove-service [SERVICE-ID]: remove a service")
print("\tshow-services [SERVICE-ID]: show a specific service")
print("\tshow-services: show services")
print("\nNAT")
print("\tnew-nat-rule: To create a new NAT rule")
print("\tremove-nat-rule: remove a NAT rule")
print("\tshow-nat: show the configured NAT rules")
print("\tshow-nat [NAT-RULE-ID] for statistics of a rule: show the statistics for a specific NAT rule")
print("\nPublic IP addressing")
print("\tnew-sddc-public-ip: request a new public IP")
print("\tremove-sddc-public-ip: remove an existing public IP")
print("\tset-sddc-public-ip: update the description of an existing public IP")
print("\tshow-sddc-public-ip: show the public IPs")
print("\nSDDC")
print("\tget-access-token: show your access token")  
print("\tshow-sddc-state: get a view of your selected SDDC")
print("\tshow-sddcs: display a lit of your SDDCs")
print("\tshow-vms: get a list of your VMs")
print("\nUser and Group management")
print("\tadd-users-to-csp-group [GROUP_ID] [EMAILS]: CSP user to a group")
print("\tshow-csp-group-diff [GROUP_ID] [showall|skipmembers|skipowners]: this compares the roles in the specified group with every user in the org and prints out a user-by-user diff")
print("\tshow-csp-group-members [GROUP_ID]: show CSP group members")
print("\tshow-csp-groups: To show CSP groups")
print("\tshow-csp-org-users [email]: show a CSP user")
print("\tshow-csp-service-roles: show CSP service roles for the currently logged in user")
print("\tfind-csp-user-by-service-role [service role name]: search for CSP users with a specific service role")
print("\tshow-org-users: show the list of organization users")
print("\nVirtual Machine Networking")
print("\tshow-network: show your current networks")
print("\tnew-network [NAME] [DISCONNECTED] [GATEWAY_ADDRESS]  for a disconnected network")
print("\tnew-network [NAME] [EXTENDED] [GATEWAY_ADDRESS] [TUNNEL_ID] for an extended network")
print("\tnew-network [NAME] [ROUTED] [GATEWAY_ADDRESS] [DHCP_RANGE] [DOMAIN_NAME] for a DHCP network")
print("\tnew-network [NAME] [ROUTED] [GATEWAY_ADDRESS] for a static network")
print("\tremove-network: remove a network")
print("\nVPN")
print("\tnew-l2vpn [NAME] [LOCAL_ENDPOINT] [REMOTE_PEER]: create a new L2VPN")
print("\tremove-l2VPN [ID]: remove a L2VPN")
print("\tremove-vpn [VPN-ID]: remove a VPN")
print("\tremove-vpn-ike-profile [ID]: remove a VPN IKE profile")
print("\tremove-vpn-ipsec-tunnel-profile [ID]: To remove a VPN IPSec Tunnel profile")
print("\tshow-l2vpn: show l2 vpn")
print("\tshow-l2vpn-services: show l2 vpn services")
print("\tshow-vpn: show the configured VPN")
print("\tshow-vpn [VPN_ID]: show the VPN statistics")
print("\tshow-vpn-ike-profile: show the VPN IKE profiles")
print("\tshow-vpn-internet-ip: show the public IP used for VPN services")
print("\tshow-vpn-ipsec-tunnel-profile: show the VPN tunnel profile")
print("\tshow-vpn-ipsec-endpoints: show the VPN IPSec endpoints")