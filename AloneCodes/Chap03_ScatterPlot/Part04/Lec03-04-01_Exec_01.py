import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.spines import Spine


np.random.seed(0)

n_data = 20
n_point = 200
scale = 3

x_mean_list = np.random.randint(-60, 60, n_data)
y_mean_list = np.random.randint(-60, 60, n_data)

cmap: LinearSegmentedColormap = cm.get_cmap('rainbow', lut=n_data)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 15))

for data_idx in range(n_data):
    x_data = np.random.normal(loc=x_mean_list[data_idx],
                              scale=scale,
                              size=(n_point,))
    y_data = np.random.normal(loc=y_mean_list[data_idx],
                              scale=scale,
                              size=(n_point,))

    # scatter plotting
    ax.scatter(x_data, y_data,
               color=cmap(data_idx),
               alpha=0.5)

# tick & ticklabel customizing
x_ticks = np.arange(-60, 61, 20)
y_ticks = np.arange(-60, 61, 20)

ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.tick_params(axis='both',
               labelsize=20,
               length=8,
               width=3)

# spine customizing
spine: Spine
for spine_loc, spine in ax.spines.items():
    spine.set_linewidth(3)
    spine.set_alpha(0.5)

fig.tight_layout()
plt.show()
