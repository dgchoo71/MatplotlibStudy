# Colorbar의 tick 위치를 변경하기

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
Z1 = np.power(X, 2) + np.power(Y, 2)
Z2 = np.power(X, 3) + np.power(Y, 3)

levels1 = np.linspace(np.min(Z1), np.max(Z1), 30)
cmap1: LinearSegmentedColormap = cm.get_cmap('Reds_r', lut=len(levels1))

levels2 = np.linspace(np.min(Z2), np.max(Z2), 30)
cmap2: LinearSegmentedColormap = cm.get_cmap('Blues_r', lut=len(levels2))

fig: Figure
ax: np.ndarray

# colorbar를 그릴 경우에는 colorbar가 위치할 공간을 고려해야 한다.
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 7))

# 첫번째 차트
cf1 = axes[0].contourf(X, Y, Z1, levels=levels1, cmap=cmap1)
# colorbar를 어느 축에 적용할지를 명시해야 한다.
cbar1 = fig.colorbar(cf1, ax=axes[0])

# 두번째 차트
cf2 = axes[1].contourf(X, Y, Z2, levels=levels2, cmap=cmap2)
# colorbar를 어느 축에 적용할지를 명시해야 한다.
cbar2 = fig.colorbar(cf2, ax=axes[1])

fig.show()
plt.close(fig)
