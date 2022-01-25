# Linewidth
# Linestyle = {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure
ax: Axes

# region
fig, ax = plt.subplots(figsize=(7, 7))
ax.grid(axis='x', linewidth=2, linestyle=':', color='r')

fig.show()
plt.close(fig)
# endregion

# region
fig, ax = plt.subplots(figsize=(7, 7))
ax.grid(axis='x', linewidth=2, linestyle='--', color='g')

fig.show()
plt.close(fig)
# endregion

# region
fig, ax = plt.subplots(figsize=(7, 7))
ax.grid(axis='x', linewidth=2, linestyle='-.', color='b')

fig.show()
plt.close(fig)
# endregion


