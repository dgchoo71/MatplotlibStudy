# 여러 개의 차트에 그리기


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np
import numpy.typing as npt


PI = np.pi
t: np.ndarray = np.linspace(-4 * PI, 4 * PI, 1000).reshape(1, -1)
sin: np.ndarray = np.sin(t)
cos: np.ndarray = np.cos(t)
tan: np.ndarray = np.tan(t)
data: np.ndarray = np.vstack((sin, cos, tan))

title_list: list = [r'$sin(t)$', r'$cos(t)$', r'$tan(t)$']
x_ticks: np.ndarray = np.arange(-4 * PI, 4 * PI + PI, PI)
x_ticklabels: list = [str(i) + r'$\pi$' for i in range(-4, 5)]

fig: Figure
axes: npt.NDArray[Axes]
# X 축을 공유하는 차트들 생성한다.
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 10), sharex=True)

ax: Axes
for ax_idx, ax in enumerate(axes.flat):
    ax.plot(t.flatten(), data[ax_idx])
    ax.set_title(title_list[ax_idx], fontsize=30)
    ax.tick_params(labelsize=20)
    ax.grid()
    if ax_idx == 2:
        ax.set_ylim([-3, 3])
        
fig.subplots_adjust(left=0.1, right=0.95, bottom=0.05, top=0.95)

axes[-1].set_xticks(x_ticks)
axes[-1].set_xticklabels(x_ticklabels)

fig.show()
plt.close(fig)
