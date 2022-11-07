import numpy as np
import matplotlib.pyplot as plt
import math

'''Uses trig functions and matplotlib to display shapes'''

appname = "trigplot - "
winsize = 7

def circle(cycles=0):
    coslist = []
    sinlist = []
    cycles = 0
    for x in np.arange(0.0,(2*math.pi)+0.1,0.1):
        coslist.append(math.cos(x))
        sinlist.append(math.sin(x))
    plt.figure(makelabel("Circle",cycles),figsize = (winsize,winsize))
    plt.plot(coslist, sinlist)
    plt.xticks([])
    plt.yticks([])
    plt.show()

def sine(cycles=1):
    list = []
    for x in np.arange(0.0,(cycles*2*math.pi)+0.1,0.1):
        list.append(math.sin(x))
    plt.figure(makelabel("Sine",cycles),figsize = (winsize,winsize))
   # plt.axis("off")
    plt.xticks([])
    plt.yticks([])
    plt.plot(list)
    plt.show()

def cosine(cycles=1):
    list = []
    for x in np.arange(0.0,(cycles*2*math.pi)+0.1,0.1):
        list.append(math.cos(x))
    plt.figure(makelabel("Cosine",cycles),figsize = (winsize,winsize))
    plt.plot(list)
    #plt.axis("off")
    plt.xticks([])
    plt.yticks([])
    plt.show()

def tangent(cycles=1):
    list = []
    for x in np.arange(0.0,(cycles*2*math.pi)+0.1,0.1):
        list.append(math.tan(x))
    plt.figure(makelabel("Tangent",cycles),figsize = (winsize,winsize))
    plt.plot(list)
    #plt.axis('off')
    plt.xticks([])
    plt.yticks([])
    plt.show()

def makelabel(name,cycles):
    if cycles == 0:
        cyclabel = ""
        cycles = ""
    elif cycles == 1:
        cyclabel = " (" + str(cycles) + " Cycle)"
    else:
        cyclabel = " (" + str(cycles) + " Cycles)"
    return appname + name + cyclabel