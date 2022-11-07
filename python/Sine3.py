from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

setHz = 10

t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(t, sin((setHz*2)*pi*t))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Seconds')
ax1.set_title('Sine Wave')

for label in ax1.get_xticklabels():
    label.set_color('k')

show()