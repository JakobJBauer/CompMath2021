import matplotlib.pyplot as plt
import numpy as np

circle = False
ellipse = not circle

l = np.arange(0, 2 * np.pi, np.pi/10)       # winkel
k = np.arange(0, 1, 0.05)                   # abstand
colors = np.array(["red", "green", "blue", "yellow", "black", "orange", "purple", "brown", "gray", "cyan", "magenta"])

fig = plt.figure()

if circle:
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    j = 0
    for i in k:
        x = []
        y = []
        for r in l:
            x.append(i * (np.cos(r)))
            y.append(i * (np.sin(r)))
        ax1.scatter(x, y, c=colors[j], s=9, marker="o")
        j = (j+1) % len(colors)

    ax1.legend(("circles",))
    ax1.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax1.set_yticks([-1, -0.5, 0, 0.5, 1])


if ellipse:
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    j = 0
    for i in k:
        x = []
        y = []
        for r in l:
            x.append(i * (np.cos(r)))
            y.append(i * (np.sin(r)) * 0.5)
        ax2.scatter(x, y, c=colors[j], s=9, marker="o")
        j = (j+1) % len(colors)

    ax2.legend(("ellipses",))
    ax2.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax2.set_yticks([-1, -0.5, 0, 0.5, 1])
plt.show()
