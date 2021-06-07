import matplotlib.pyplot as plt
import numpy as np

# a
fig = plt.figure()

# b
plot1 = fig.add_axes([0.11, 0.11, 0.35, 0.8])
plot2 = fig.add_axes([0.6, 0.11, 0.35, 0.8])

# c
plot1.set_xlabel('x')
plot1.set_ylabel('y = x²')

plot2.set_xlabel('x')
plot2.set_ylabel('y = x')

plot1.set_title('first plot')
plot2.set_title('second plot')

values = np.arange(0, 2, 0.1)

plot1.plot(values, values**2, color='r')
plot2.plot(values, values)

plot1.legend(['x²'])
plot2.legend(['x'])

fig.show()

# d
"""
plt.gca returns the current Axes
plt.gcf returns the current Figure
"""
