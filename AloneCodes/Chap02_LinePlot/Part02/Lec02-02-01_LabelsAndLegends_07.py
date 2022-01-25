import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np

sys.path.append('../../../')

from AloneCodes.Chap02_LinePlot.bop_utils import *


dataset: np.ndarray = bop_data_reader()
t_year_list: list = [1990, 1992, 1994, 1996, 1998]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(14, 10))

for t_year_idx, t_year in enumerate(t_year_list):
    t_data: np.ndarray = get_year_data(dataset, t_year)
    
    ax.plot(t_data[:, -1], label=f'Year {t_year}')
    
ax.legend(loc='upper left', fontsize=20)

major_yticks = np.arange(10, 41, 10)
minor_yticks = np.arange(10, 43, 2)

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)
ax.tick_params(axis='y', length=10, labelsize=20)

ax.grid(axis='y', which='major')
ax.grid(axis='y', which='minor', linestyle=':')

ax.set_ylabel('daily prices in USD', fontsize=15)
fig.show()

# legend 위치 변경
ax.legend(loc='center left',
          bbox_to_anchor=(1, 0.5),
          fontsize=20)
fig.tight_layout()
fig.show()
