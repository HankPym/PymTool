import requests  
import json
from datetime import datetime

r = requests.get('https://api.track.toggl.com/reports/api/v2/summary/details?workspace_id=3834475&since=2021-08-29&until=2021-09-04&user_agent=api_test', auth=('6c30ab3d9f8de3d22b3028ac327a134f', 'api_token'))



rj = r.json()
#print(rj)
for i in rj['data']:	
	project = i['title']['project']
	print(project)
	duration = i['time']
	print(int(duration)//60000)
