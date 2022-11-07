myNum = 5
myDenom = 0

try:
	print(myNum/myDenom)
except ZeroDivisionError:
	print( "Error: Cannot divide by zero (", myNum,"/", myDenom, ")" )

