import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


# data setting
data = [
    dict(label='filter/natural test',
         values=[50, 65, 70, 75, 76],
         marker='v',
         linecolor='r',
         linestyle='-'),
    dict(label='column/natural test',
         values=[61, 68, 70, 74, 76],
         marker='^',
         linecolor='g',
         linestyle='-'),
    dict(label='irregular/natural test',
         values=[76, 78, 77, 78, 76],
         marker='s',
         linecolor='c',
         linestyle='-'),
    dict(label='filter/adversarial test',
         values=[34, 38, 41, 42, 43],
         marker='o',
         linecolor='r',
         linestyle='--'),
    dict(label='column/adversarial test',
         values=[36, 40, 42, 43, 43],
         marker='+',
         linecolor='g',
         linestyle='--'),
    dict(label='irregular/adversarial test',
         values=[42, 41, 44, 44, 43],
         marker='x',
         linecolor='c',
         linestyle='--')
]

x_loc = [2 ** i for i in range(5)]

# plotting
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xscale('log', base=2)

for data_idx, data_dict in enumerate(data):
    ax.plot(x_loc,
            data_dict['values'],
            color=data_dict['linecolor'],
            linewidth=2,
            marker=data_dict['marker'],
            markersize=15,
            linestyle=data_dict['linestyle'],
            label=data_dict['label'])

# legend 위치 및 설정
ax.legend(loc='lower center',
          bbox_to_anchor=(0.5, 0),
          ncol=2,
          fontsize=25)

# spine 설정
spine: Spine
for spine_idx, spine in enumerate(ax.spines.values()):
    spine.set_linewidth(3)
    
# tick * ticklabel 설정
x_ticks = [2 ** i for i in range(5)]
x_ticklabels = x_ticks
y_ticks = [20 * i for i in range(6)]
y_ticklabels = y_ticks

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels, fontsize=30)

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticklabels, fontsize=30)

ax.set_ylim((0, 100))

# 축의 label 설정
label_dict = {'size': 40}
ax.set_xlabel('w', fontdict=label_dict)
ax.set_ylabel('Accuracy (%)', fontdict=label_dict)

fig.show()


