# Brent Oil 가격을 그래프로 그리기
import sys

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np

# bop_utils 를 찾을 경로를 추가한다.
# ternimal에서 실행하기 위해 package path를 추가한다.
sys.path.append('../../../')
from AloneCodes.Chap02_LinePlot.bop_utils import *


dataset: np.array = bop_data_reader()
t_year = 1990
t_year_data: np.array = get_year_data(dataset, t_year)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(t_year_data[:, -1])   # 가격 정보만 출력

ax.set_title(f'BOP data ({t_year})', fontsize=30)
ax.set_ylabel('daily prices in USD', fontsize=25)
ax.tick_params(labelsize=20)

# y축의 그리드만 표시
ax.grid(axis='y')

fig.show()

plt.close(fig)


