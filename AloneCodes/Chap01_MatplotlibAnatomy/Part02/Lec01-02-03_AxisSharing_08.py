# row-wise, column-wise로 축을 공유하기

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.axis import Axis

import numpy.typing as npt

fig: Figure = plt.figure(figsize=(10, 10))

n_rows, n_cols = 3, 3
axes: npt.NDArray[npt.NDArray] = np.empty(shape=(0, 3))

for r_idx in range(n_rows):
    axes_row: npt.NDArray[Axes] = np.empty(shape=(0,))
    
    for c_idx in range(n_cols):
        ax: Axes = fig.add_subplot(n_rows, n_cols, r_idx * n_rows + c_idx + 1)
        
        # 두번째 열의 축들은 첫번째 열의 Y 축을 공유한다
        if c_idx > 0:
            ax.sharey(axes_row[0])
            
        # 두번째 행의 축들은 첫번째 행의 X 축을 공유한다.
        if r_idx > 0:
            ax.sharex(axes[0][c_idx])
            # ax.sharex(axes[0, c_idx])
    
        axes_row = np.append(axes_row, ax)
        
    axes = np.vstack([axes, axes_row])
    
# 기준이 되는 축의 범위 설정
axes[0, 0].set_xlim([0, 10])
axes[0, 1].set_xlim([0, 20])
axes[0, 2].set_xlim([0, 30])

axes[0, 0].set_ylim([0, 100])
axes[1, 0].set_ylim([0, 200])
axes[2, 0].set_ylim([0, 300])


fig.tight_layout()
fig.show()

