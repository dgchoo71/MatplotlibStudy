# Axis Layout Adjustment

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig, ax = plt.subplots(figsize=(7, 7))

fig: Figure = fig
ax: Axes = ax

ax.set_title('Title !', fontsize=20)
ax.set_xlabel('X Label !', fontsize=15)
ax.set_ylabel('Y Label !', fontsize=15)

fig.show()
