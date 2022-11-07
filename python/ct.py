import random

runTimeMinutes = 60
vialsPerHour = 3000
inspectionGroups = 27
inspectionTimeSeconds = 30
percentBad = 3

inspectionGroupList = []
for loopCounter in range(0,inspectionGroups):
	inspectionGroupList.append(0)
runTimeSeconds = runTimeMinutes * 60
goodBin = 0
badBin = 0

minuteCount = 0
readyForInspection = 0

for timeCounter in range(0,runTimeSeconds):
	if (timeCounter < vialsPerHour):
		readyForInspection = readyForInspection + 1
		if (timeCounter % 60)==0:
			minuteCount = minuteCount + 1
			# print minuteCount, "Minutes -", readyForInspection, "vials remaining. "

	for inspectionRound in range (0,inspectionGroups):
		vialsUnderInspection = 0
		if ( (readyForInspection > 0) and (inspectionGroupList[inspectionRound] == 0) ):
			inspectionGroupList[inspectionRound] = timeCounter + inspectionTimeSeconds
			badChance = random.randint(1,100)
			if badChance <= percentBad:
				inspectionGroupList[inspectionRound] = inspectionGroupList[inspectionRound] + 10
				badBin = badBin + 1
			else:
				goodBin = goodBin + 1
			readyForInspection = readyForInspection - 1
			vialsUnderInspection = vialsUnderInspection + 1
		if inspectionGroupList[inspectionRound] == timeCounter:
			inspectionGroupList[inspectionRound] = 0
			vialsUnderInspection = vialsUnderInspection - 1


	if (timeCounter > inspectionGroups and readyForInspection == 0):
		break

endMinutes = timeCounter / 60

print("Total Time:", endMinutes, "Minutes \n",readyForInspection, "vials remaining.\n", goodBin + badBin, " total vials.\n", goodBin, " good vials.\n", badBin, " bad vials.")
