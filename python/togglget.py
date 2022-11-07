import requests  
import json
from datetime import datetime

r = requests.get('https://api.track.toggl.com/reports/api/v2/details?workspace_id=3834475&since=2021-08-29&until=2021-09-04&user_agent=api_test', auth=('6c30ab3d9f8de3d22b3028ac327a134f', 'api_token'))

dates = {}
projects = {}
durations = {}

rj = r.json()
for i in rj['data']:
	#start = i['start']
	date = datetime.strptime(i['start'][:10],'%Y-%m-%d').date()
	project = i['project']
	#print(project)
	duration = i['dur'] // 60000.0
	print(project,",",date,",",duration)
	if project in projects:
		current = projects[project]
		projects[project] = current + (duration)
	else:
		projects[project] = duration

print(projects)
