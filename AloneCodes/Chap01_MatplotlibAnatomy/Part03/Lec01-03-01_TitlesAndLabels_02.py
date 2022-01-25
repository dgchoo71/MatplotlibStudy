# Figure title, axes title, axes label

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


figsize = (7, 7)
ax_title_list = [f'Title {i}' for i in range(4)]

fig: Figure; axes: np.ndarray
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=figsize)

fig.suptitle("Title of a Figure", fontsize=40,
             fontfamily="monospace")

for ax_idx, ax in enumerate(axes.flat):
    ax: Axes = ax
    ax.set_title(ax_title_list[ax_idx],
                 fontsize=30, fontfamily="serif")

# Figure의 title과 ax의 title이 일부 겹쳐져서 그려지게 된다.
fig.show()

# Title의 영역이 자동으로 조절이 되어 그려지게 된다.
fig.tight_layout()
fig.show()

# 조금 더 적극적으로 크기를 조절할 수 있다.
fig.subplots_adjust(bottom=0.05, top=0.8, hspace=0.3)
fig.show()
