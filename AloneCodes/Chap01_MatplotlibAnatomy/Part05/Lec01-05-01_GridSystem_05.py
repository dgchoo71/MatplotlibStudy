# Major and minor tick
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


major_yticks = [i for i in range(0, 101, 20)]
minor_yticks = [i for i in range(0, 101, 5)]
ytick_labels = [f'{i} %' for i in major_yticks]

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)
ax.set_yticklabels(ytick_labels)

ax.tick_params(labelsize=20)

ax.grid(axis='y', which='major', linewidth=1.5)
ax.grid(axis='y', which='minor', linestyle=':')

fig.subplots_adjust(left=0.15)

fig.show()
plt.close(fig)

