inspection_NumberOfInspectors = 20
inspection_SecondsToGetTray = 8
inspection_SecondsPerVial = 11
inspection_SecondsToPutTray = 8

production_VialsPerTray = 7
production_MaxNumberOfVials = 7500

time_MaxAllowableMinutes = 180
time_TransferFromMixingMinutes = 20
time_TransferToCRFMinutes = 15
time_MinutesBetweenBreaks = 60
time_BreakMinutes = 10

# Do not edit below this line! -----------------------------------------------------------

maxSeconds = (time_MaxAllowableMinutes * 60) - (time_TransferFromMixingMinutes * 60) - (time_TransferToCRFMinutes * 60)

maxSecondsBetweenBreaks = time_MinutesBetweenBreaks * 60
maxBreakSeconds = time_BreakMinutes * 60
secondsPerSet = (inspection_SecondsPerVial * production_VialsPerTray) + inspection_SecondsToGetTray + inspection_SecondsToPutTray
inspected = 0
vialsFilled = 0
vialSets = 0
setsInInspection = 0
vialsInInspection = 0
inspectionsCompletedFlag = 0
totalSeconds = 0
readyToInspect = 0
vialsNotTrayed = 0
untrayedVialsInspected = 0
breakTime = 0

arrInspectors = [0 for x in range(inspection_NumberOfInspectors)]

for seconds in range(1,maxSeconds):
	if (vialsFilled < production_MaxNumberOfVials):
		vialsFilled = vialsFilled + 1
		vialsNotTrayed = vialsNotTrayed + 1
		if (vialsFilled % production_VialsPerTray == 0):		
			readyToInspect = readyToInspect + 1
			vialsNotTrayed = 0
	if ( (inspectionsCompletedFlag == 1) and (vialsNotTrayed > 0) ):
		untrayedVialsInspected = untrayedVialsInspected + 1
		vialsNotTrayed = vialsNotTrayed - 1

	if (seconds % maxSecondsBetweenBreaks == 0):
		breakTime = maxBreakSeconds
	if (breakTime > 0):
		breakTime = breakTime - 1
	else:
		for cycles in range(0,inspection_NumberOfInspectors):
			if (( arrInspectors[cycles] == 0) and (readyToInspect > 0)):
				arrInspectors[cycles] = 1
				readyToInspect =  readyToInspect - 1
			elif ( (arrInspectors[cycles] > 0) and (arrInspectors[cycles] < secondsPerSet ) ):
				arrInspectors[cycles] = arrInspectors[cycles] + 1
			elif (arrInspectors[cycles] == secondsPerSet):
				inspected = inspected + 1
				arrInspectors[cycles] = 0
			else:
				True
	if ( (vialsFilled >= production_MaxNumberOfVials) and (readyToInspect == 0) and (inspectionsCompletedFlag == 0) ):
		totalSeconds = seconds
		inspectionsCompletedFlag = 1

for cycles in range(0,inspection_NumberOfInspectors):
	if (arrInspectors[cycles] > 0):
		setsInInspection = setsInInspection + 1
vialsInInspection = setsInInspection * production_VialsPerTray

print "Vials filled: ", vialsFilled
print "\tTrays/Vials inspected: ",inspected,"/",(inspected * production_VialsPerTray) + untrayedVialsInspected
print "\tTrays/Vials awaiting inspection: ", readyToInspect, "/", (readyToInspect * production_VialsPerTray) + vialsNotTrayed
print "\tTrays/Vials in inspection: ",setsInInspection, "/",vialsInInspection
print "\n"
if (totalSeconds > 0):
	print "Completion time: ",totalSeconds/60, "minutes"
	print "\tRemaining time: ", ((maxSeconds - totalSeconds)/60)+1, "minutes"
else:
	print "THE MAXIMUM ALLOWABLE TIME OF", time_MaxAllowableMinutes, "MINUTES HAS BEEN EXCEEDED."