import matplotlib.pyplot as plt
import numpy as np

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

plt.rc('axes', labelsize=10)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

x = np.arange(-2, 2, 0.01)

ax1.set_xlabel('x')
ax1.plot(x, np.sin(4*x), color='r')
ax1.legend(['sin(4x)'], loc='center right')
plt.setp(ax1.get_xticklabels(), visible=False)

ax2.set_xlabel('x')
ax2.plot(x, np.cos(x)*np.sin(x))
ax2.legend(['cos(x)sin(x)'], loc='center')
plt.setp(ax2.get_xticklabels(), visible=False)

ax3.set_xlabel('x')
ax3.plot(x, np.cos(x))
ax3.legend(['cos(x)'], loc='lower center')

ax4.set_xlabel('x')
ax4.plot(x, np.cos(x)+np.sin(x))
ax4.legend(['cos(x)+sin(x)'], loc='lower right')

fig.show()
