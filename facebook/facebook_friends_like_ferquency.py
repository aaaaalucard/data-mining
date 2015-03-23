import json
import facebook
from prettytable import PrettyTable
from collections import Counter
from operator import itemgetter
"""
This example prints out the top X friends like and their categories
First, query all the likes in your social network

get_object('me', fields= 'id, name, friends.fields(id, name ,likes)' )

"""
ACCESS_TOKEN = 'CAACEdEose0cBAGnbaAOyZA8E0Y2WDavBGwtYcEEzo8MjfSbqFMAURfP9VcleHULXiyjOxOA7ABaK3FseheAZASuS1ejyTG1khy16iXAunBHWsdzCg1E6XgZCZBofhD8faBKOhoTkVnHzZBts7ACIH8cs9Q8UmpSf7HNwIAPXtJXZCY8wZBrz7xsK0XS99tKXpMZC59RN0r46jiYVgrgMrSic4ZCa9lcOTC6UZD'
facebook_api = facebook.GraphAPI(ACCESS_TOKEN)

def pp(out):
    print json.dumps(out , indent = 1)

friends = facebook_api.get_connections("me", "friends")['data']


likes = {friend['name']: facebook_api.get_connections(friend['id'], "likes")['data']
               for friend in friends }
#faster when using facebook's api
# likes = facebook_api.get_object('me', fields = 'id, name, friends.fields(id, name, likes)')

pp(likes)

for friend in likes:
    print len(likes[friend])

# friends_likes = Counter( [like['name']
#                                         for friend in likes
#                                             for like in likes[friend]
#                                                  ])


# friends_likes_categories = Counter( [like['name'] for friend in likes for like in likes[friend] ])




# pt = PrettyTable(field_names = ['Name', 'Freq'])
# pt.align['Name'], pt.align['Freq'] = 'l', 'r'
# [  pt.add_row(row) for row in friends_likes.most_common(10)  ]
# # [  pt.add_row(row) for row in friends_likes_categories.most_common(10)  ]

# print "Top 10 friend likes"
# print pt

# num_likes_by_friend = { friend : len(likes[friend])
#                                         for friend in likes
                                         
# }

# pt2 = PrettyTable(field_names = ['Friend', 'Num_likes'])
# pt2.align['Name'], pt2.align['Freq'] = 'l', 'r'
# [  pt2.add_row(row) for row in sorted(num_likes_by_friend.items(), key = itemgetter(1), 
#                                                         reverse = True)  ]

# print pt2