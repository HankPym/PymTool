from matplotlib.patches import CirclePolygon
import numpy as np
import matplotlib.pyplot as plt
import math

def mycircle():
    myA = []
    myB = []
    for x in np.arange(0.0,(2*math.pi)+0.1,0.1):
        myA.append(math.cos(x))
        myB.append(math.sin(x))
    plt.figure("Trig Circle",figsize = (5,5))
    plt.plot(myA, myB)
    plt.show()

mycircle()
   