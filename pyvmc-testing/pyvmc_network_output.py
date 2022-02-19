
import requests                         # need this for Get/Post/Delete
import configparser                     # parsing config file
import operator
import time
import json
import sys
from deepdiff import DeepDiff
from os.path import exists
from prettytable import PrettyTable

def showt0routes(t0_routes):
    route_table = PrettyTable(['Route Type', 'Network', 'Admin Distance', 'Next Hop'])
    for routes in t0_routes:
        route_table.add_row([routes['route_type'],routes['network'],routes['admin_distance'],routes['next_hop']])
    print ('T0 Routes')
    print ('Route Type Legend:')
    print ('t0c - Tier-0 Connected\nt0s - Tier-0 Static\nb   - BGP\nt0n - Tier-0 NAT\nt1s - Tier-1 Static\nt1c - Tier-1 Connected\nisr: Inter-SR')
    print (route_table.get_string(sort_key = operator.itemgetter(1,0), sortby = "Network", reversesort=True))

def showt0prefixlists(prefixlists):
    for prefixlist in prefixlists:
        prefixlisttable = PrettyTable(['ID','Display Name','Description'])
        prefixlisttable.add_row([prefixlist["id"],prefixlist["display_name"],prefixlist["description"]])
        print("PREFIX:")
        print(prefixlisttable)
        prefixtable = PrettyTable(['Sequence','Network','Comparison', 'Action'])
        i = 0
        if prefixlist.get('prefixes'): 
            for prefix in prefixlist['prefixes']:
                i+=1
                if prefix.get('ge'):
                    comparison = "ge (greater-than-or-equal)"
                elif prefix.get('le'):
                    comparison = "le (less-than-or-equal)"
                else:
                    comparison = '-'
                prefixtable.add_row([i,prefix['network'],comparison,prefix['action']])
            print(f'PREFIX ENTRIES FOR {prefixlist["id"]}:')
            print(prefixtable)
            print("")
    if len(sys.argv) == 3:
        if sys.argv[2] == "showjson":
            print('RAW JSON:')
            print(json.dumps(prefixlists,indent=2))
    else:
        print("No user created prefixes found.")
