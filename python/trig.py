import numpy as np
import math
import matplotlib.pyplot as plt

trigRange= np.linspace(0,2*math.pi,100)

fig = plt.figure(figsize=(10,7))
sinPoints = np.array(np.sin(trigRange))
cosPoints = np.array(np.cos(trigRange))
plt.plot(sinPoints, 'g', label='Sine')
plt.plot(cosPoints, 'r--', label='Cosine')
plt.legend(loc=3)

plt.show()