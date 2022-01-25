# Colorbar의 tick를 변경하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap

import numpy as np


x = np.linspace(-10, 10, 100)
y = x

X, Y = np.meshgrid(x, y)
Z = np.power(X, 2) + np.power(Y, 2)

levels = np.linspace(np.min(Z), np.max(Z), 30)

fig: Figure
ax: Axes

cmap: LinearSegmentedColormap = cm.get_cmap('Reds_r', lut=len(levels))

# colorbar를 그릴 경우에는 colorbar가 위치할 공간을 고려해야 한다.
fig, ax = plt.subplots(figsize=(8, 7))
cf = ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
cbar = fig.colorbar(cf)   # contour의 color를 추가한다.

# colorbar의 tick 설정
cbar_ticks = cbar.get_ticks()
# tick을 3 구간으로 분할
new_cbar_ticks = np.linspace(cbar_ticks[0], cbar_ticks[-1], 3)

# 새로운 tick을 적용
cbar.set_ticks(new_cbar_ticks)

# tick label도 변경할 수 있다.
cbar.set_ticklabels(['low', 'medium', 'high'])
cbar.ax.tick_params(labelsize=20)  # tick의 크기 변경

fig.show()
plt.close(fig)
