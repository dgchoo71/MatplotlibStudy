# 다른 API 와 비교하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# add_subplot
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_subplot(211)
ax2: Axes = fig.add_subplot(223)
ax3: Axes = fig.add_subplot(224)
fig.show()

# subplot2grid
plt.clf()
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = plt.subplot2grid((2, 2), (0, 0), colspan=2, fig=fig)
ax2: Axes = plt.subplot2grid((2, 2), (1, 0), fig=fig)
ax3: Axes = plt.subplot2grid((2, 2), (1, 1), fig=fig)
fig.show()
