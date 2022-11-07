''' PyPlotPlaytime'''
import math as m
import matplotlib.pyplot as plt
import numpy as np

show   = 1   # 1 = show sin/cos, 2 = show histogram, 3 = show both
cycles = 1   # Number of sin/cos cycles

# Create and plot sine and cosine waves
if (show == 1 or show == 3):
    sinColor = "blue"
    cosColor = "red"
    scCycles= cycles * (m.pi * 2) 
    sinlist = []
    coslist = []
    for point in np.arange(0., (scCycles), 0.001):
        sinlist.append(m.sin(point))
        coslist.append(m.cos(point))
    plt.figure('Sine and Cosine')
    plt.plot(sinlist, linewidth=2, color=sinColor)
    plt.plot(coslist, linewidth=2, color=cosColor)
    plt.figtext(0.33, 0.90, "Sine",   fontsize='large', fontweight='bold', color=sinColor, ha ='right')
    plt.figtext(0.66, 0.90, "Cosine", fontsize='large', fontweight='bold', color=cosColor, ha ='left')

# Create and plot a histogram
if (show == 2 or show == 3):
    plt.figure('Histogram')
    histo = np.random.normal(0, 0.1, 10000)
    plt.hist(histo)
    plt.title("Histogram")

plt.show()