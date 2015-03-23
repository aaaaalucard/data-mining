import json
import facebook

ACCESS_TOKEN = 'CAACEdEose0cBAMF7BPBnA3ZA9ZADxHZCaMU3q2Bjovl7jZChBMO6RFetrkZAlTF0KWxOkQq1esrpmtSAMu2qncZAPbB5xC5zZAmimZBDNxSqics2h7UScCMXuqOEhodk7q5C4Ml3loXssOtdB3PZBFmTdPVzS6rK0hnZChGZCPPINIH9Cskwt7ILmQePBuvksBiORB7tvtrMd4KFekcV4QDSyzi'

def pp(out):
    print json.dumps(out , indent = 1)

facebook_api = facebook.GraphAPI(ACCESS_TOKEN)

# print '-------------------------------------'
# print 'Me'
# pp(facebook_api.get_object('me'))
# print '-------------------------------------'


# print 'My Friends'
# pp(facebook_api.get_connections('me', 'likes'))
# print '-------------------------------------'
# print 'Social Web'
# pp(facebook_api.request("search", {'q' : 'social web', 'type' : 'page'}))


mtsw_id = '146803958708175'
#pp(facebook_api.get_object(mtsw_id))
pp(facebook_api.get_object('http://shop.oreilly.com/product/0636920030195.do'))