from fredapi import Fred
import pandas as pd
import math
pd.options.display.max_rows =600

fred = Fred(api_key='40141301f4b0cb485199d02951b8ae09')

#df = fred.get_series_all_releases('CUURA100SAF') # food and beverage
#df= fred.get_series_all_releases('CUURA100SA0E') # energy
df = fred.get_series_all_releases('CUURA100SAC') # commodities
#df = fred.get_series_all_releases('CUURA100SAS') # services
df = df.dropna()
#services.set_index([0],inplace=True)
df = df.reset_index()

alldata = ""

for index, row in df.iterrows():
	currentDate = row['date'].date()
	currentVal = row['value']
	if (index == 0):
		currentShift = 0
	else:
		currentShift = currentVal - lastVal 
	alldata = alldata + str(currentDate) + ',' + str(currentVal) + '\n'
	lastVal = currentVal
		
filename = open("commodities.csv","w")
n = filename.write(alldata)
filename.close()
