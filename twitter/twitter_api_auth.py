import twitter

"""
Exercise 1.1:use OAuth credentials to gain authorization to query twitter api
go to dev.twitter.com/apps/ find own apps to get all the secure information needed to authentication
"""

CONSUMER_KEY = 'EvuitjxetTseyAhyC11ag'
CONSUMER_SECRET = 'e8NUQdjtr3uXGVXM5r2hUfpXLVTdyOwGH5wWYgIX2g'
OAUTH_TOKEN = '2174723124-EtGw4uJCZ7hoHJKmS8BMz9z1nlJMGeYi8ebd4wd'
OAUTH_TOKEN_SECRET = 'aRR95kcbKW21s0eZhSmpClbD5wx6Ytx3YCFJKJZJzRqjt'

#code body
def get_twitter_api():
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                                CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth = auth)
    print twitter_api
    return twitter_api

if __name__ == '__main__':
    get_twitter_api()