import networkx as nx 
import facebook
import requests
import json


ACCESS_TOKEN = 'CAACEdEose0cBAGnbaAOyZA8E0Y2WDavBGwtYcEEzo8MjfSbqFMAURfP9VcleHULXiyjOxOA7ABaK3FseheAZASuS1ejyTG1khy16iXAunBHWsdzCg1E6XgZCZBofhD8faBKOhoTkVnHzZBts7ACIH8cs9Q8UmpSf7HNwIAPXtJXZCY8wZBrz7xsK0XS99tKXpMZC59RN0r46jiYVgrgMrSic4ZCa9lcOTC6UZD'

facebook_api = facebook.GraphAPI(ACCESS_TOKEN)

friends = [(friend['id'], friend ['name'],)
                for friend in facebook_api.get_connections('me', 'friends')['data']]

print friends
# url = 'https://graph.facebook.com/me/mutualfriends/%s?access_token=%s'

# mutual_friends = {}

# for friend_id, friend_name in friends:
#     r = requests.get(url % (friend_id, ACCESS_TOKEN,)  )
#     response_data = json.loads(r.content)['data']
#     mutual_friends[friend_name] = [data['name'] for data in response_data ]

# #print mutual_friends
# print 
# nxg = nx.Graph()

# [nxg.add_edge('me', mf) for mf in mutual_friends]

# [nxg.add_edge(f1,f2)
#     for f1 in mutual_friends
#         for f2 in mutual_friends[f1]]

# #finding cliques
# cliques = [c for c in nx.find_cliques(nxg)]
# num_cliques = len(cliques)
# clique_sizes = [len(c) for c in cliques]
# max_clique_size = max(clique_sizes)
# avg_clique_size = sum(clique_sizes) / num_cliques
# max_cliques = [c for c in cliques if len(c) == max_clique_size]
# num_max_cliques = len(max_cliques)
# max_clique_sets = [set(c) for c in max_cliques]

# friends_in_all_max_cliques = list(reduce(lambda x, y: x.intersection(y), max_clique_sets))

# print "Number of cliques", num_cliques
# print "Average clique size", avg_clique_size
# print "Max clique size", max_clique_size
# print"Number of max cliques", num_max_cliques 
# print
# print "Friend in all max cliques:"
# print json.dumps(friends_in_all_max_cliques, indent = 1)
# print 
# print "Max cliques:"
# print json.dumps(max_cliques, indent = 1)
# from networkx.readwrite import json_graph

# nld = json_graph.node_link_data(nxg)
# json.dump(nld, open('force.json', 'w'))

# """
# from IPython.display import IFrame
# from IPython.core.display import display
# viz_file = 'force.html'
# display(IFrame(viz_file, '100%', '600px'))
# """