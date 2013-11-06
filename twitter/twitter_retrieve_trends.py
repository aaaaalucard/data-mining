import twitter
import twitter_api_auth
import json #for a nicer display
"""
Exercise 1.2 to 1.4:
Explore trends and topics.
Documents at : https://dev.twitter.com/docs/api/1.1/get/trends/place
Use Yahoo! WOE id.
"""

WORLD_WOE_ID =1
US_WOE_ID = 23424977

def get_world_trends():
    twitter_api = twitter_api_auth.get_twitter_api();
    world_trends = twitter_api.trends.place(_id = WORLD_WOE_ID)
    print json.dumps(world_trends, indent = 1)
    return world_trends

def get_us_trends():
    twitter_api = twitter_api_auth.get_twitter_api();
    us_trends = twitter_api.trends.place(_id = US_WOE_ID)
    print json.dumps(us_trends, indent = 1)
    return us_trends

'''
Improvement:
Parse out the names of the trending topics.
List to set.
'''
def parse_trend(world_trends,us_trends):
    # only the name of the trending topics is left
    world_trends_set = set([trend['name']
                                        for trend in world_trends[0]['trends']])
    us_trends_set = set([trend['name']
                                        for trend in us_trends[0]['trends']])
    #get the topic both in world and us
    common_trends = world_trends_set.intersection(us_trends_set)
    print common_trends
    return common_trends

if __name__ == '__main__':
    world_trends = get_world_trends()
    us_trends = get_us_trends()
    parse_trend(world_trends, us_trends)
