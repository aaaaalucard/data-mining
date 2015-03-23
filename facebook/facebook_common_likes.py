from prettytable import PrettyTable
import facebook
from collections import Counter
from operator import itemgetter
import pylab


ACCESS_TOKEN = 'CAACEdEose0cBALaZAUSNqQKMXdID5h7btOYNgciIcJ7ilCN6q17WudxHdSfZCJ459Dm2fEa0096SqmWscztWfseyyO7JTnppUMstZBeCIPbhlxpIFm6UajdPB5bwk4xv3XdYW3WU2zQLuFXeWmAgCpWxzjibkmcNIW5RXptEiybRBiDGQKJ59fmPDdgs5UR3BDj7kOnNgZDZD'

facebook_api = facebook.GraphAPI(ACCESS_TOKEN)
my_likes = [ like['name']
                        for like in facebook_api.get_connections("me", "likes")['data']
]

#print my_likes
pt = PrettyTable(field_names = ['Name'])
pt.align = 'l'
[pt.add_row((row,)) for row in my_likes] # not number here
print pt

friends = facebook_api.get_connections("me", "friends")['data']


likes = {friend['name']: facebook_api.get_connections(friend['id'], "likes")['data']
               for friend in friends }

friends_likes = Counter( [like['name']
                                        for friend in likes
                                            for like in likes[friend]
                                                 ])

common_likes = list(set(my_likes)&set(friends_likes))
pt = PrettyTable(field_names = ['Name'])
pt.align = 'l'
[pt.add_row((row,)) for row in common_likes] # not number here
print pt

similar_friends = [(friend, friend_like['name'])
                                for friend, friend_likes in likes.items()
                                    for friend_like in friend_likes
                                        if friend_like.get('name') in common_likes]

ranked_friends = Counter([friend for (friend, like) in list(set(similar_friends))])
pt = PrettyTable(field_names = ['Friend', 'Name'])
pt.align["Friend"], pt.align["Name"] = 'l', 'r'
[ pt.add_row (rf)
    for rf in sorted(ranked_friends.items(),
                            key = itemgetter(1),
                            reverse = True)]

print pt