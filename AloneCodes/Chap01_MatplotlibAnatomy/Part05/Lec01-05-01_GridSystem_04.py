# Major and minor tick
# tick을 먼저 설정하고 grid를 설정한다.
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


major_ticks = [i for i in range(0, 101, 20)]
minor_ticks = [i for i in range(0, 101, 5)]

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)

ax.tick_params(labelsize=20)

ax.grid(axis='x', which='major', linewidth=1.5)
ax.grid(axis='x', which='minor', linestyle=':')

fig.show()
plt.close(fig)

