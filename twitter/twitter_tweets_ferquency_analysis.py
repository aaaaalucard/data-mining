import twitter
import json
from collections import Counter
import twitter_search_tweet
from prettytable import PrettyTable

"""
Creating a basic frequency count based on the words in tweets
"""

def frequency_count(tweet_entities):    
    status_texts = tweet_entities.status_texts
    screen_names = tweet_entities.screen_names
    hashtags = tweet_entities.hashtags
    words = tweet_entities.words

    for item in [words, screen_names, hashtags]:
        c = Counter(item)
        print c.most_common()[0:10] #top 10
        print 

def frequency_count_table(tweet_entities):
    

    status_texts = tweet_entities.status_texts
    screen_names = tweet_entities.screen_names
    hashtags = tweet_entities.hashtags
    words = tweet_entities.words    
    for label, data in (('Word', words),
                                ('Screen_names', screen_names),
                                ('Hashtags', hashtags)):
        pt = PrettyTable(field_names = [label, 'Count'])
        c = Counter(data)
        [ pt.add_row(kv) for kv in c.most_common()[:10] ]
        pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
        print pt

#function for lexical diversity
#shows the percentage of unique words. lower means less diversity
def lexical_diversity(tokens):
    return 1.0*len(set(tokens))/len(tokens)

#function for computing the average number of words per tweet
def average_words(statuses):
    total_words = sum([len(status.split()) for status in statuses])
    return 1.0*total_words/len(statuses)

def find_retweet(statuses):
    retweets = [ (status['retweet_count'],
                        status['retweeted_status']['user']['screen_name'],
                        status['text'])

                        for status in statuses if status.has_key('retweeted_status')
                        ]
    pt = PrettyTable(field_names = ['Count', 'Screen_name', 'Text'])
    [ pt.add_row(kv) for kv in sorted(retweets, reverse = True)[:5] ]
    pt.max_width['text'] = 50
    pt.align = 'l'
    print pt


if __name__ == '__main__':
    tweet_entities = twitter_search_tweet.tweet_parse(twitter_search_tweet.tweet_search(twitter_search_tweet.q))
    frequency_count_table(tweet_entities)

    print lexical_diversity(tweet_entities.words)
    print lexical_diversity(tweet_entities.hashtags)
    print lexical_diversity(tweet_entities.screen_names)
    print average_words(tweet_entities.status_texts)
    print
    find_retweet(twitter_search_tweet.tweet_search(twitter_search_tweet.q))