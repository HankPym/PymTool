# This script calculates pi by executing the Nilakantha Series for the defined number of cycles.
# Nilakantha Series: = pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14) ...

import math

cycles = int(input("How many cycles?  "))

loopCount = 2.0
cycleCount = 0
piValue = 3.0

while (cycleCount < cycles):
	if (cycleCount%2 == 0):
		# Add on even cycles
		piValue = piValue + 4.0/(loopCount*(loopCount+1)*(loopCount+2))
	else:
		# Subtract on odd cycles
		piValue = piValue - 4.0/(loopCount*(loopCount+1)*(loopCount+2))
	cycleCount = cycleCount + 1
	loopCount = loopCount + 2

print(piValue)

