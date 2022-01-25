# 뷸규칙한 형식의 Axes 만들기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


# 단일 축 그리기
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

# 전체 그리그 크기, 축을 생성할 위치, 축을 생성할 Figure를 인자로 사용
ax1: Axes = plt.subplot2grid((1, 1), (0, 0), fig=fig)
plt.show()
plt.close(fig)

# 세로로 배치된 두 개의 축을 그리기
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax1: Axes = plt.subplot2grid((2, 1), (0, 0), fig=fig)
ax2: Axes = plt.subplot2grid((2, 1), (1, 0), fig=fig)
plt.show()
plt.close(fig)

# 가로로 배치된 두 개의 축을 그리기
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
ax1: Axes = plt.subplot2grid((1, 2), (0, 0), fig=fig)
ax2: Axes = plt.subplot2grid((1, 2), (0, 1), fig=fig)
plt.show()
plt.close(fig)