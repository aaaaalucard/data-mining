import json
import facebook

ACCESS_TOKEN = 'CAACEdEose0cBAGRY4goGq6c2Lqf3rtmzJL4Mzmu0ToDqdNJf8I2G0bAR8vfZAavP02Dw46G1ciWZBllHxsWDN4b1uk3JozkoN0ZATk0agCCBxh8I1zLVBdZC3Wf2vIo7bLQbhcqy4Iy8dvZAiMl529ewO1OhMgNnxxU7WjeCPgnkSKmWfL3tw4sJQQpkBWoYtrwrcPExieOlb9NfK0B6P'
pepsi_id = 'PepsiUS'
coke_id = 'CocaCola'

def pp(out):
    print json.dumps(out , indent = 1)

facebook_api = facebook.GraphAPI(ACCESS_TOKEN)

# pp(facebook_api.request('search', {'q':'pepsi', 'id':56381779049 ,'type': 'page','limit': 5}))
# pp(facebook_api.request('search', {'q':'coke', 'type': 'page','limit': 5}))

# doc = facebook_api.request('search', {'q':'pepsi', 'id':56381779049 ,'type': 'page','limit': 5})
# pp(facebook_api.get_object(pepsi_id))

# print doc.get('likes')
print "Pepsi Liked:", (int)(facebook_api.get_object(pepsi_id)['likes']) 
print "Coke Liked:", (int)(facebook_api.get_object(coke_id)['likes']) 

# print help(facebook_api)

pp(facebook_api.get_connections(pepsi_id, 'feed')['data'])
# pp(facebook_api.get_connections(pepsi_id, 'likes'))

# pp(facebook_api.get_connections(coke_id, 'feed'))
# pp(facebook_api.get_connections(coke_id, 'links'))
