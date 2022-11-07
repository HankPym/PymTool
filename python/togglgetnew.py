import requests  
import json
from datetime import datetime
from datetime import timedelta

until = '2021-09-04'
untilAsDT = datetime.strptime(until,'%Y-%m-%d').date()
since = str(untilAsDT - timedelta(days=6))

request = "https://api.track.toggl.com/reports/api/v2/details?workspace_id=3834475&since="+since+"&until="+until+"&user_agent=api_test'"
r = requests.get(request,auth=('6c30ab3d9f8de3d22b3028ac327a134f', 'api_token'))

dates = []
projects = []
durations = []
keys = []

rj = r.json()
for i in rj['data']:
	date = datetime.strptime(i['start'][:10],'%Y-%m-%d').date()
	project = i['project']
	duration = i['dur'] // 60000.0
	dates.append(date)
	projects.append(project)
	durations.append(duration)
	keys.append(str(date)+project+str(duration))
	
keyCount = len(keys)
	
for outer in range(0,keyCount):
	for inner in range(0, keyCount-1):
		if (keys[inner] > keys[inner+1]):

			temp = keys[inner]
			keys[inner] = keys[inner+1]
			keys[inner+1] = temp
			
			temp = dates[inner]
			dates[inner] = dates[inner+1]
			dates[inner+1] = temp
			
			temp = projects[inner]
			projects[inner] = projects[inner+1]
			projects[inner+1] = temp
			
			temp = durations[inner]
			durations[inner] = durations[inner+1]
			durations[inner+1] = temp

lines = keyCount-1

try:
	for x in range(0,lines):
			if( (dates[x] == dates[x+1]) and (projects[x] == projects[x+1]) ):
				durations[x] = durations[x] + durations[x+1]
				dates.pop(x+1)
				projects.pop(x+1)
				durations.pop(x+1)
				lines = lines - 1

except IndexError:
	for x in range(0,len(dates)):
		print(dates[x],projects[x],round(durations[x]/60.0,2))


