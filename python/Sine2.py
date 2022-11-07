import matplotlib.pyplot as plt
import numpy
import math

def sinewave(z):
	cycles = z*2

	y_range = [math.sin(x) for x in numpy.arange(0,cycles*math.pi,0.01)]
	x_range = numpy.arange(numpy.size(y_range))
	plt.plot(x_range,y_range)
	
	plt.title("Sine")
	
	if (z > 1):
		label = " cycles"
	else:
		label = " cycle"
	
	plt.xlabel(str(z) + label)
	plt.xticks([])
	plt.show()

sinewave(2)