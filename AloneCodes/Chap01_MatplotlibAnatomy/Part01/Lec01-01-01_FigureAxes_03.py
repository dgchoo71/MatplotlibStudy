# 불규칙한 Axes 배열 만들기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_subplot(2, 2, 1)
ax2: Axes = fig.add_subplot(2, 2, 2)
ax3: Axes = fig.add_subplot(2, 1, 2)

plt.show()

# ----
# 다른 형태
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = fig.add_subplot(2, 3, 1)
ax2: Axes = fig.add_subplot(2, 3, 2)
ax3: Axes = fig.add_subplot(2, 3, 4)
ax4: Axes = fig.add_subplot(2, 3, 5)

# 오른쪽의 큰 Axes 추가
ax5: Axes = fig.add_subplot(1, 3, 3)

plt.show()

