import matplotlib.pyplot as plt
from numpy import arange, sin, pi
t = arange(0.0, 1.0, 0.001)
plt.plot(t, sin(2*pi*t))
plt.xlabel('Sine')
plt.show()