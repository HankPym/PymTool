from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim((-1.1, 1.1))
ax1.set_ylabel('One Cycle',color='blue')

# Change the first plot ticks to red
#for label in ax1.get_xticklabels():
#    label.set_color('r')


ax2 = fig.add_subplot(212)
ax2.plot(t, sin(2*2*pi*t),'g')
ax2.grid(True)
ax2.set_ylim((-1.1, 1.1))
ax2.set_ylabel('Two Cycles',color='green')

ax1.set_title('A Sine Wave or Two...')

show()