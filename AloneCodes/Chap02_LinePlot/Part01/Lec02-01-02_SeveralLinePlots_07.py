# 여러 차트에 라인 데이터 그리기

import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np
import numpy.typing as npt


# ternimal에서 실행하기 위해 package path를 추가한다.
sys.path.append('../../../')

from AloneCodes.Chap02_LinePlot.bop_utils import *


def bop_plot(dataset: np.ndarray, t_year: float, ax: Axes):
    t_year_data: np.ndarray = get_year_data(dataset, t_year).astype(np.int_)
    
    month_dict = {m:None for m in range(1, 1 + 12)}
    for data_idx, data in enumerate(t_year_data):
        Y, M, D, price = data
        if month_dict[M] is None:
            month_dict[M] = [data_idx, '-'.join(str(i) for i in [Y, M, D])]
            
    first_day_label = np.array(list(month_dict.values()))
    
    x_arange = np.arange(t_year_data.shape[0])
    ax.plot(x_arange, t_year_data[:, -1])   # 가격 데이터 출력
    ax.set_xticks(first_day_label[:, 0].astype(np.int_))
    ax.set_xticklabels(first_day_label[:, -1], rotation=-30, ha='left')
    ax.set_title('BOP data ({})'.format(t_year), fontsize=30)
    
    ax.tick_params(labelsize=20)
    ax.grid()
    
    
dataset: np.array = bop_data_reader()
t_year_list: list = [1990, 1991, 1995]
fig: Figure
axes: npt.NDArray[Axes]
fig, axes = plt.subplots(nrows=len(t_year_list), ncols=1, figsize=(15, 10))

ax: Axes
for ax_idx, ax in enumerate(axes.flat):
    bop_plot(dataset, t_year_list[ax_idx], ax)
    
    if ax_idx == 1:
        ax.set_ylabel("daily prices in USD", fontsize=25)

fig.tight_layout()
fig.show()
plt.close(fig)
