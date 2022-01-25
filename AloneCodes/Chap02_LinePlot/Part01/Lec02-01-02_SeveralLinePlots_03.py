# 하나의 차트에 여러 개의 Line Plot 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np


PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 300)
sin = np.sin(t)
linear = 0.1 * t

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(t, sin)
ax.plot(t, linear)

fig.show()

# y축 방향의 limit 설정
ax.set_ylim([-1.5, 1.5])

x_ticks = np.arange(-4 * PI, 4 * PI + 0.1, PI)
x_ticklabels = [f'{i} $\pi$' for i in range(-4, 5)]

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels)

ax.tick_params(labelsize=20)
ax.grid()

fig.show()
