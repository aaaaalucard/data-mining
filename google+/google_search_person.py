import httplib2
import json
import apiclient.discovery

Q = "Mengchen Zhang"
API_KEY = 'AIzaSyDOVsZmTOjSXonrbtKAhmY-AZkmZUzirwA'
#invoke the People API
service = apiclient.discovery.build('plus', 'v1', http = httplib2.Http(), developerKey = API_KEY)

people_feed = service.people().search(query = Q).execute()
print json.dumps(people_feed['items'], indent = 1)

#print out those results with user pictures
from IPython.core.display import HTML
html = []
for p in people_feed['items']:
    html += ['<p><img src = "%s /> %s: %s</p>' % \
                    (p['image']['url'], p['id'], p['displayName'])]
HTML(' '.join(html))

