# 여러 개의 axis를 생성하기
# Grid System

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# Figure는 하나의 그래프를 그릴 수 있는 전체 canvas이다.
# Figure를 생성할 때 크기를 지정할 수 있다. (인치 단위)
# Figure의 색상도 지정할 수 있다.
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

# Rows, Columns, i-th axes
ax: Axes = fig.add_subplot(111)

# 또는
ax: Axes = fig.add_subplot(1, 1, 1)
fig.show()
plt.close(fig)

# ---------
# 3 X 1 Axes 생성하기
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_subplot(311)
ax2: Axes = fig.add_subplot(312)
ax3: Axes = fig.add_subplot(313)

ax1.plot([2, 5, 10])
ax2.plot([10, 5, 2])

fig.show()
plt.close(fig)

# ------------
# 2 X 2 Axes 생성하기
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_subplot(2, 2, 1)
ax2: Axes = fig.add_subplot(2, 2, 2)
ax3: Axes = fig.add_subplot(2, 2, 3)
ax4: Axes = fig.add_subplot(2, 2, 4)

fig.show()
plt.close(fig)
