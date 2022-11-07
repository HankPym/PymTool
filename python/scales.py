import sys
strInput = sys.argv[1]
if (strInput == "?"):
	print("Usage: scales.py \"scale data\"")
	print("       Use \"_\" for data to ingore.")
	print("       Use \"0\" for numeric data to be read.")
else:
	intLength = len(strInput)
	strOutput = ""
	for count in range(intLength):
		if (count > 0):
			strOutput = strOutput + "|"
		strLine = str(ord(strInput[count]))
		if (strLine == "95"):
			strLine = "64"
		if (strLine == "48"):
			strLine = "35"
		if (strLine == "46"):
			strLine = "35"
		strOutput = strOutput + strLine
	strOutput = strOutput + "|13|10"
	print(strOutput)
