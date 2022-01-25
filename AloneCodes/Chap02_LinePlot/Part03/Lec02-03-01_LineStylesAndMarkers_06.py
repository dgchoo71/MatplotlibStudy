# Line Marker Customizing

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 50)
sin = np.sin(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin + 1,
        marker='o',
        color='black',
        markersize=15,
        markerfacecolor='r',
        markeredgecolor='b',
        markeredgewidth=3)

fig.show()
