import matplotlib, matplotlib.pyplot as pyplot
import numpy
import types
import math


def simple():

    for x in range(100):
        y = math.sqrt(x)
        pyplot.scatter(x, y, lw=2)

    axes = pyplot.gca()
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    pyplot.show()

simple()