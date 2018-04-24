import urllib, json
url = "http://seaswimdash.marsec.services/feed/departures?numberOfDays=2&route=VAL-SF&route=VAL-Pier41&route=Pier41-SF"
response = urllib.urlopen(url)
sched_dict = (json.loads(response.read()))
print sched_dict
