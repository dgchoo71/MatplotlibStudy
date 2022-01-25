# Axis Layout Adjustment

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes


title_list = [f'Ax {i}' for i in range(4)]
xlabel_list = [f'X Label {i}' for i in range(4)]
ylabel_list = [f'Y Label {i}' for i in range(4)]


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
fig: Figure = fig
axes: np.ndarray = axes

for ax_idx, ax in enumerate(axes.flat):
    ax: Axes = ax
    ax.set_title(title_list[ax_idx], fontsize=20)
    ax.set_xlabel(xlabel_list[ax_idx], fontsize=15)
    ax.set_ylabel(ylabel_list[ax_idx], fontsize=15)
    
# 크기 조정이 안 된 상태로 축들이 생성된다.
fig.show()

# 축들의 크기와 위치를 조정한다.
fig.tight_layout()
fig.show()

# 패딩 조정: 축들 사이의 간격 조정
fig.tight_layout(pad=0.3)
fig.show()

fig.tight_layout(pad=3)
fig.show()

fig.tight_layout(pad=5)
fig.show()

