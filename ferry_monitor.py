import requests
import json

#set schedule variable for boats going SF->Vallejo
sched = requests.get('http://seaswimdash.marsec.services/feed/departures?numberOfDays=2&route=VAL-SF&route=VAL-Pier41&route=Pier41-SF')

#set variable for parsed json version of lineup 
sched_json = sched.json()

#print json object
print sched_json