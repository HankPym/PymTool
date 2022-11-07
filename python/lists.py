gradeDict = {"Fred":92,"Joe":87,"Linda":96}

print("Number of keys:",len(gradeDict))

print("Fred ->",gradeDict["Fred"])

print(gradeDict.keys())

for key in gradeDict:
    print(key, '->',gradeDict[key])

theAverage = sum(gradeDict.values()) / len(gradeDict)

print("Average:",round(theAverage,2))
