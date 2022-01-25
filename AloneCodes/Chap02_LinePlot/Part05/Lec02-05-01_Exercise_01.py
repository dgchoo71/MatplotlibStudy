import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


# rcParams setting
plt.rcParams['lines.linewidth'] = 2

# data setting
x_loc = np.linspace(2.5, 20, 8)
data = np.array(
    [[30, 37, 40, 46.5, 46.5, 46, 45.5, 45],
     [47.5, 48, 47.6, 47.3, 47, 46.6, 46.3, 46],
     [52, 52.5, 53, 53, 53, 53, 53, 53],
     [60.5, 61, 60.5, 60, 59.8, 59.6, 59.4, 59.2]])

name_list = [f'Part {i}' for i in range(4)]

# customizing setting
color_list = ['tab:blue', 'tab:red', 'tab:green', 'tab:orange']

# plotting
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

for line_idx in range(len(name_list)):
    ax.plot(x_loc, data[line_idx],
            color=color_list[line_idx],
            label=name_list[line_idx])

# customizing
ax.set_ylim([28, 62])
ax.set_title('IoU over number of experts', fontsize=15)
ax.legend(loc='lower right', fontsize=15)
ax.tick_params(labelsize=15)

fig.tight_layout()
fig.show()
    