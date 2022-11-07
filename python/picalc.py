myCycles = int(input("Enter the number of cycles:"))
myPercent = myCycles / 100
denom = float(1)
piCalc = float(4/denom)
myCount = 1

print("Running...")

while (denom < myCycles):
	denom = denom + 2
	piCalc = piCalc - float(4/denom)
	denom = denom + 2
	piCalc = piCalc + float(4/denom)
print(piCalc)
