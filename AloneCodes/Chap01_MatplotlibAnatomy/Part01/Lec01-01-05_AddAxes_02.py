# 여러 축을 추가하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

rect1 = [0.1, 0.1, 0.5, 0.5]
rect2 = [0.7, 0.1, 0.2, 0.5]
rect3 = [0.1, 0.7, 0.8, 0.2]

fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_axes(rect1)
ax2: Axes = fig.add_axes(rect2)
ax3: Axes = fig.add_axes(rect3)
fig.show()
