import matplotlib.pyplot as plt
import numpy as np

# a
fig = plt.figure()

ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.2, 0.5, .2, .2])

# b
data = np.arange(0, 100)

ax1.plot(data, 2*data, color='r')
ax1.legend(['x²'])
ax1.set_xlabel('x')
ax1.set_ylabel('x²')

ax2.set_title('zoom')
ax2.plot(data, 2*data, color='r')
ax2.set_xlabel('x')
ax2.set_ylabel('x²')
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])

fig.show()
