# 연습문제 1
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_yscale('log')
ax.set_ylim([1, 1E4])

ax.tick_params(labelsize=20, length=10)
ax.tick_params(which='major', length=5)

ax.grid(axis='y', which='major', linewidth=1.5)
ax.grid(axis='y', which='minor', linestyle=':')

fig.show()
plt.close(fig)

