# 임의의 X 데이터 사용하기
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np


np.random.seed(0)

x_data = np.array([10, 25, 31, 40, 55, 80, 100])
y_data = np.random.normal(0, 1, (len(x_data),))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_data, y_data)

fig.subplots_adjust(left=0.2)
ax.tick_params(labelsize=25)

fig.show()

# xtick 조정
ax.set_xticks(x_data)

# ytick 조정
ylim = ax.get_ylim()    # 자동으로 설정된 ylim 값을 사용
yticks = np.linspace(ylim[0], ylim[-1], len(y_data) + 1)  # tick 간격 변경
ax.set_yticks(yticks)
ax.grid()
fig.show()

plt.close(fig)
