# Ticks and Grid
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


major_ticks = [i for i in range(0, 101, 20)]


fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xticks(major_ticks)
ax.tick_params(labelsize=20)
ax.grid(axis='x', which='major', linewidth=1.5, color='r')

fig.show()
plt.close(fig)

