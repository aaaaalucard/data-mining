import json
import nltk

DATA = 'graph.json'
data = json.loads(open(DATA).read())

#print json.dumps(data, indent = 1)

QUERY_TERMS = ['SOPA']

activities = [activity['object']['content'].lower().split() \
              for activity in data \
                if activity['object']['content'] != ""]


tc = nltk.TextCollection(activities)

relevant_activities = []

for idx in range(len(activities)):
    score = 0
    for term in [t.lower() for t in QUERY_TERMS]:
        score += tc.tf_idf(term, activities[idx])
    if score > 0:
        relevant_activities.append({'score': score, 'title': data[idx]['title'],
                              'url': data[idx]['url']})

# Sort by score and display results

relevant_activities = sorted(relevant_activities, key=lambda p: p['score'], reverse=True)
for activity in relevant_activities:
    print activity['title']
    print '\tLink: %s' % (activity['url'], )
    print '\tScore: %s' % (activity['score'], )