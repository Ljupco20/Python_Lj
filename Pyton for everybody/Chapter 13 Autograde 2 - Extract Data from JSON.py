import urllib.request
import json

url = input("Enter URL: ")
response = urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8')
data = json.loads(response)
counts = list()

comments = data['comments']
for comment in comments:
    counts.append(comment['count'])

print (sum(counts))
   
   
   
   
   
