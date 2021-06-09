import matplotlib.pyplot as plt
import numpy as np


def draw_ellipse(y_scale=1.0):
    l = np.arange(0, 2 * np.pi, np.pi / 10)
    k = np.arange(0, 1, 0.05)
    colors = np.array(['#1d79af', '#fd7f0d', '#2c9c2d', '#d1272b', '#9369be', '#8a5648', '#e279be', '#7f7e7e', '#bcbc24', '#1bbfcd'])

    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    for i in range(len(k)):
        ax1.scatter(
            np.array(list(map(lambda a: k[i] * np.cos(a), l))),
            np.array(list(map(lambda a: k[i] * np.sin(a) * y_scale, l))),
            c=colors[i % len(colors)], marker="o"
        )

    ax1.legend(("circles",))
    ax1.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax1.set_yticks([-1, -0.5, 0, 0.5, 1])
    plt.show()


if __name__ == '__main__':
    draw_ellipse()            # circle
    draw_ellipse(0.5)         # ellipse
