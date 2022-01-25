# Colorbar 사용하기

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

fig.show()
plt.close(fig)
