#IMPORTING LIBRARY
from asyncore import write
import requests
import json
import pandas as pd
import csv

url_data='https://en.wikipedia.org/w/api.php?action=query&list=search&gsrlimit=50&srsearch=travel&format=json'
Header = { 'Accept' : 'application/json',
        'content-Type':'application/json'}
reaaponce = requests.request("GET",url_data,headers=Header,data={})
myjosn = reaaponce.json()
pagelist = []
rawlist = {}
col_name = ['ns','title','pageid','size','wordcount','snippet','timestamp']
"""
for x in myjosn['query']['pages']:
        rawlist.append(myjosn['query']['pages'][x])
for raw in rawlist:
        pagelist.append(raw)
# with open('wikirecords.csv','w',encoding='UTF8',newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(col_name)
#         writer.writerows(rawlist)
"""
for x in myjosn['query']['search']:
        pagelist.append(x)
with open('wiki.csv','w',newline='',encoding="UTF8") as csvfile:
        writer = csv.DictWriter(csvfile,col_name)
        writer.writeheader()
        writer.writerows(pagelist)
print("done")