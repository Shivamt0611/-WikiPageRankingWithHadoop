#IMPORTING LIBRARY
from asyncore import write
from turtle import done
import requests
import json
import pandas as pd
import csv

url_data='https://en.wikipedia.org/w/api.php?action=query&origin=*&format=json&generator=search&gsrnamespace=0&gsrlimit=500&gsrsearch=%27Narendra%20Modi%27'
Header = { 'Accept' : 'application/json',
        'content-Type':'application/json'}
reaaponce = requests.request("GET",url_data,headers=Header,data={})
myjosn = reaaponce.json()
pagelist = []
rawlist = []
col_name = ['pageid','ns','title','index']

for x in myjosn['query']['pages']:
        rawlist.append(myjosn['query']['pages'][x])
for raw in rawlist:
        pagelist.append(raw)
        # with open('wikirecords.csv','w',encoding='UTF8',newline='') as f:
        #         writer = csv.writer(f)
        #         writer.writerow(col_name)
        #         writer.writerows(pagelist)
with open('wiki.csv','w',newline='',encoding="UTF8") as csvfile:
        writer = csv.DictWriter(csvfile,col_name)
        writer.writeheader()
        writer.writerows(pagelist)
print('Done')