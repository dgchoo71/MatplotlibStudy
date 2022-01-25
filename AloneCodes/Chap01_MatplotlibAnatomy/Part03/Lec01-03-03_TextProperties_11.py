# Title, label and Font Dict 연습 문제 2

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


title_list = ['Blurry image', 'Ours', 'Mohan et al. [23]']

fig: Figure
axes: np.ndarray = np.empty((0, 4))

fig = plt.figure(figsize=(24, 10))

n_groups, n_cols, n_rows = 3, 4, 5
shape = (5, 12)

g_idx: int
ax: Axes
for g_idx in range(n_groups):
    axes_row: np.ndarray = np.empty((0,))
    
    axes_row = np.append(axes_row,
                         plt.subplot2grid(
                             shape=shape, loc=(0, g_idx * n_cols),
                             colspan=n_cols, rowspan=3, fig=fig))
    axes_row = np.append(axes_row,
                         plt.subplot2grid(
                             shape=shape, loc=(3, g_idx * n_cols),
                             colspan=3, rowspan=2, fig=fig))
    axes_row = np.append(axes_row,
                         plt.subplot2grid(
                             shape=shape, loc=(3, g_idx * n_cols + 3), fig=fig))
    axes_row = np.append(axes_row,
                         plt.subplot2grid(
                             shape=shape, loc=(4, g_idx * n_cols + 3), fig=fig))

    # 축 서식 감추기
    for ax in axes_row:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        
    # 전체 배열에 쌓기
    axes = np.vstack([axes, axes_row])
    
    # 그룹의 타이틀을 설정하기
    axes_row[0].set_title(title_list[g_idx], fontsize=30, y=-0.83)
    
fig.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.95,
                    hspace=0.05, wspace=0.05)
fig.show()
