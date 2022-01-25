# X 축의 레이블 표시

import sys

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np

# ternimal에서 실행하기 위해 package path를 추가한다.
sys.path.append('../../../')

from AloneCodes.Chap02_LinePlot.bop_utils import *

dataset: np.array = bop_data_reader()
t_year = 1990
t_year_data: np.array = np.array(get_year_data(dataset, t_year)).astype(np.int32)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))

# 날짜를 생성하기 위한 딕셔너리 정의
month_dict = {m: None for m in range(1, 12 + 1)}

for data_idx, data in enumerate(t_year_data):
    Y, M, D, price = data
    if month_dict[M] is None:   # 월의 첫번째 날짜가 설정이 안 되어 있는 경우라면
        month_dict[M] = [data_idx, '-'.join(str(i) for i in [Y, M, D])]
        
first_day_label = np.array(list(month_dict.values()))
x_arange = np.arange(t_year_data.shape[0])  # X 축값의 개수

ax.plot(x_arange, t_year_data[:, -1])   # 가격 정보만 출력

ax.set_xticks(np.array(first_day_label[:, 0]).astype(np.int32))
ax.set_xticklabels(first_day_label[:, 1], rotation=-30, ha='left')

ax.set_title(f'BOP data ({t_year})', fontsize=30)
ax.set_ylabel('daily prices in USD', fontsize=25)
ax.tick_params(labelsize=20)
ax.grid()

fig.show()
plt.close(fig)


