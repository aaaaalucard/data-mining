# -*- coding: utf-8 -*-
import httplib2
import json
import apiclient.discovery

USER_ID = '107033731246200681024'
API_KEY = 'AIzaSyDOVsZmTOjSXonrbtKAhmY-AZkmZUzirwA'

service = apiclient.discovery.build('plus', 'v1', http = httplib2.Http(), developerKey = API_KEY)

activity_feed = service.activities().list(
    userId = USER_ID,
    collection = 'public',
    maxResults = '100',

).execute()

print json.dumps(activity_feed, indent = 1)


