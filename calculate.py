import sys

# define function to perform mathematical order of operations
# (powers, multiplication, division, addition, subtraction)
def pmdas(inString):
	while (not(inString.replace(".","").replace("-","").isdigit())):
		arrValues = inString.split(" ")
		intSize = len(arrValues)-1
		strActions = "^ * / + -"
		arrActions = strActions.split(" ")
		for intAction in range(0,len(arrActions)):
			currentAction = arrActions[intAction]
			for intPlace in range(0,intSize):
				if arrValues[intPlace] == currentAction:
					strCurrent = arrValues[intPlace-1] + " " + arrValues[intPlace] + " " + arrValues[intPlace+1]
					if currentAction == "^":
						intResult2 = str(float(arrValues[intPlace-1]) ** float(arrValues[intPlace+1]))
					elif currentAction == "*":
						intResult2 = str(float(arrValues[intPlace-1]) * float(arrValues[intPlace+1]))
					elif currentAction == "/":
						intResult2 = str(float(arrValues[intPlace-1]) / float(arrValues[intPlace+1]))
					elif currentAction == "+":
						intResult2 = str(float(arrValues[intPlace-1]) + float(arrValues[intPlace+1]))
					elif currentAction == "-":
						intResult2 = str(float(arrValues[intPlace-1]) - float(arrValues[intPlace+1]))
					inString = inString.replace(strCurrent,intResult2)
					arrValues = inString.split(" ")
					intSize = len(arrValues)-1
	return inString

if len(sys.argv) > 1:
	strIn = sys.argv[1]
	print("\nIn[1]:  " + strIn)
	# First, handle values within parenthesis
	while (strIn.find("(") > -1):
		intParenStart = 0
		for intCurrent in range(0,strIn.find(")")+1):
			#	print(strIn)
			strCurChar = strIn[intCurrent]
			if (strCurChar=="("):
				intParenStart = intCurrent+1
			elif (strCurChar==")"):
				intRange = intCurrent-intParenStart-1
				strCurr = strIn[intParenStart-1:intCurrent+1]
				strCont = strIn[intParenStart:intCurrent]
				intResult = pmdas(strCont)
				strIn = strIn.replace(strCurr,str(intResult))
			intCurrent = 0
			
	# Perform final pmdas and print output
	intFinal = pmdas(strIn)	
	print("\nOut[1]: " + intFinal + "\n")

else:
	print("\nNeed input.\n")