# Axes의 facecolor 사용

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_subplot(311, facecolor='r')
ax2: Axes = fig.add_subplot(3, 1, 2, facecolor='g')
ax3: Axes = fig.add_subplot(3, 1, 3, facecolor='b')

plt.show()

