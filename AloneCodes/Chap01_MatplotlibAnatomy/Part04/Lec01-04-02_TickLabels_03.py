# Tick Labels 연습문제 2

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


yticks = np.arange(0.4, 0.54, 0.02)
xticks = [i for i in range(8)]
xtick_labels = [
    " ",
    "FC-Agg 1 layer",
    "FC-Agg 2 layer",
    "Topo-Agg 0-hop",
    "Topo-Agg 0-hop test only",
    "Topo-Agg 1-hop",
    "Topo-Agg 2-hop",
    " "
]

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(20, 10))

ax.set_yticks(yticks)
ax.set_ylim([0.4, 0.52])

# tick의 위치를 먼저 설정하고 난 뒤, 레이블을 설정한다
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels, ha='right')

ax.tick_params(axis='x', rotation=20, labelsize=15, colors='gray')
ax.tick_params(axis='y', labelsize=15, colors='gray')

ax.set_ylabel("mAP: Unseen Scenes", fontsize=20, color='gray')

fig.subplots_adjust(bottom=0.15)

fig.show()
