# 연습 문제

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

left, bottom = 0.1, 0.1
spacing = 0.005

width1, height1 = 0.65, 0.65
width2 = 1 - (2 * left + width1 + spacing)
height2 = 1 - (bottom + height1 + spacing + bottom)

rect1 = [left, bottom, width1, height1]
rect2 = [left + width1 + spacing, bottom, width2, height1]
rect3 = [left, bottom + height1 + spacing, width1, height2]

fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_axes(rect1)
ax2: Axes = fig.add_axes(rect2)
ax3: Axes = fig.add_axes(rect3)

fig.show()
