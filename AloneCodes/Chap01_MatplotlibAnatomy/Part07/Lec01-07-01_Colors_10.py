# Auto Colormap

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

# 기본 colormap
fig, ax = plt.subplots(figsize=(7, 7))
ax.contourf(X, Y, Z, levels=levels)
fig.show()
plt.close(fig)

#
cmap: LinearSegmentedColormap = cm.get_cmap('rainbow', lut=len(levels))
fig, ax = plt.subplots(figsize=(7, 7))
ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
fig.show()
plt.close(fig)

#
cmap: LinearSegmentedColormap = cm.get_cmap('Reds_r', lut=len(levels))
fig, ax = plt.subplots(figsize=(7, 7))
ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
fig.show()
plt.close(fig)

#
cmap: LinearSegmentedColormap = cm.get_cmap('hot', lut=len(levels))
fig, ax = plt.subplots(figsize=(7, 7))
ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
fig.show()
plt.close(fig)
