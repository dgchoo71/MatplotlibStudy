# add_axes를 이용하여 생성한 축 공유하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure(figsize=(7,7))

left, bottom = 0.05, 0.05
spacing = 0.05
width1, height1 = 0.6, 0.6

width2 = 1 - (2 * left + spacing + width1)
height2 = 1 - (2 * bottom + spacing + height1)

rect1 = [left, bottom, width1, height1]
rect2 = [left, bottom + height1 + spacing, width1, height2]
rect3 = [left + width1 + spacing, bottom, width2, height1]

ax1: Axes = fig.add_axes(rect1)
ax2: Axes = fig.add_axes(rect2, sharex=ax1)
ax3: Axes = fig.add_axes(rect3, sharex=ax1)

ax1.set_xlim([0, 100])
ax1.set_ylim([0, 200])

fig.show()
