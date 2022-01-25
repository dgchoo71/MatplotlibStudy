# 하나의 차트에 여러 개의 Line Plot 그리기

import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np

sys.path.append('../../../')

from AloneCodes.Chap02_LinePlot.bop_utils import *


def bop_plot(dataset: np.ndarray, t_year: int, ax: Axes):
    t_year_data: np.ndarray = get_year_data(dataset, t_year)
    ax.plot(t_year_data[:, -1])   # 가격 그래프를 그린다.
    
    
dataset: np.ndarray = bop_data_reader()

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))

bop_plot(dataset, 1990, ax)
bop_plot(dataset, 1993, ax)
bop_plot(dataset, 1996, ax)

ax.set_title("BOP data", fontsize=30)
ax.set_ylabel("daily price in USE", fontsize=25)
ax.tick_params(labelsize=20)
ax.grid()

fig.show()
