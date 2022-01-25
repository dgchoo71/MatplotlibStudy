# X축의 데이터 조정하기
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np


np.random.seed(0)

n_data = 100
s_idx = 30
x_data = np.arange(start=s_idx, stop=s_idx + n_data)
y_data = np.random.normal(loc=0, scale=1, size=(n_data,))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_data, y_data)

fig.tight_layout(pad=3)

# 데이터의 처음과 마지막의 tick을 표시하기 위해 tick을 조정한다.
x_ticks = np.arange(s_idx, s_idx + n_data + 1, 20)
ax.set_xticks(x_ticks)
ax.tick_params(labelsize=25)

ax.grid()
fig.show()
plt.close(fig)

