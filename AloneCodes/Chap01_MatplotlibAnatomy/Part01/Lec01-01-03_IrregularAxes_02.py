# 동일한 축을 3 가지 방법으로 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


# add_subplot

fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_subplot(211)
ax2: Axes = fig.add_subplot(212)
fig.show()

# subplots
plt.clf()

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(7, 7), facecolor='linen')
fig.show()

# subplot2grid
plt.clf()

fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
ax1: Axes = plt.subplot2grid((2, 1), (0, 0), fig=fig)
ax2: Axes = plt.subplot2grid((2, 1), (1, 0), fig=fig)
fig.show()

