import twitter
import twitter_api_auth
import json



#This is an example trending topic. Set as a common topic of world and us trend here.

q = '#voteaustinmahone' #A UTF-8, URL-encoded search query of 1,000 characters maximum, including operators.
count = 15 #The number of tweets to return per page, up to a maximum of 100. Defaults to 15.

class useful_information(object):
    def init(self, texts, screen_names, hashtags, words):
        self.status_texts = texts;
        self.screen_names = screen_names
        self.hashtags = hashtags
        self.words = words

def tweet_search(q):
    twitter_api = twitter_api_auth.get_twitter_api()

    #documents at https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = twitter_api.search.tweets(q = q, count = count) #Returns a collection of relevant Tweets matching a specified query.
    statuses = search_results['statuses']

    #Iterate through 5 more batches of results by following the cursor
    for _ in range(5):
        #print "The length of statuses:", len(statuses)
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e: # No more reslts when next_result doesn't exist
            break

        #Creat a dictionary from next_results
        kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

    
    return statuses

def tweet_parse(statuses):

    status_texts = [ status['text']
                             for status in statuses ]
    screen_names = [ user_mention['screen_name']
                                 for status in statuses
                                    for user_mention in status['entities']['user_mentions']]
    hashtags = [ hashtag['text']
                        for status in statuses
                            for hashtag in status['entities']['hashtags'] ]
    words = [w
                   for t in status_texts
                        for w in t.split() ]

    #print json.dumps(status_texts, indent = 1)
    #print json.dumps(screen_names, indent = 1)
    #print json.dumps(hashtags, indent = 1) 
    #print json.dumps(words, indent = 1)   
    info = useful_information()
    info.init(status_texts, screen_names, hashtags, words)
    return info

if __name__ == '__main__':
    statuses = tweet_search(q)
    info = tweet_parse(statuses)
    #print info.status_texts