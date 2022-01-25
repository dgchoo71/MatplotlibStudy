# 축의 스케일이 달라도 marker의 사이즈는 동일하다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(0, 0, s=100**2)
ax.tick_params(labelsize=20)
fig.show()

# ------------
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim((-5, 5))
ax.set_ylim((-5, 5))
ax.scatter(0, 0, s=100**2)
ax.tick_params(labelsize=20)
fig.show()

# 두 figure의 축 스케일은 다를지라도 전체 그림에서 차지하는 마커의 크기는 동일하다.
