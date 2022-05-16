# scatter 데이터의 마커를 이용하여 데이터의 크기와 종류를 표현할 수 있다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


c_arr = ['r', 'g', 'b']     # 마커의 색상
s_arr = [500, 2000, 5000]   # 마커의 크기

# 위치
x_loc = [-2, 0, 2]
y_loc = x_loc

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

for plot_idx in range(len(c_arr)):
    ax.scatter(x_loc[plot_idx], y_loc[plot_idx],
               c=c_arr[plot_idx],
               s=s_arr[plot_idx],
               label=f' data {plot_idx}')

ax.legend(loc='center left',
          bbox_to_anchor=(1.05, 0.5),
          labelspacing=10,
          fontsize=20,
          edgecolor='None')

fig.tight_layout()
plt.show()


