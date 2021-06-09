import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(-1, 1, 0.1), np.arange(-2, 1, 0.1))    # koordinaten
x_val = np.sign(x)*(1-y)
y_val = np.sign(x)*(1+x)
plt.quiver(x, y, x_val, y_val, np.hypot(x_val, y_val))
plt.title('Vector field')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
