import requests
import json
import facebook

base_url = 'https://graph.facebook.com/me'
movie_url = 'https://graph.facebook.com/http://www.imdb.com/title/tt0117500'

ACCESS_TOKEN = 'CAACEdEose0cBAMF7BPBnA3ZA9ZADxHZCaMU3q2Bjovl7jZChBMO6RFetrkZAlTF0KWxOkQq1esrpmtSAMu2qncZAPbB5xC5zZAmimZBDNxSqics2h7UScCMXuqOEhodk7q5C4Ml3loXssOtdB3PZBFmTdPVzS6rK0hnZChGZCPPINIH9Cskwt7ILmQePBuvksBiORB7tvtrMd4KFekcV4QDSyzi'
facebook_api = facebook.GraphAPI(ACCESS_TOKEN)

# get 10 likes for 10 friends
fields = 'id, name, friends.limit(3).fields(likes.limit(3))'
url = '%s?fields=%s&access_token=%s' % \
        (base_url, fields, ACCESS_TOKEN)
content = requests.get(movie_url).json()
print url

print json.dumps(content, indent = 4)

#print facebook_api.get_object("me", metadata = 1)
