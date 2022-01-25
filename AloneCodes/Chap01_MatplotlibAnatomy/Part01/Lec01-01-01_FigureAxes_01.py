# figure 객체 생성하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# Figure는 하나의 그래프를 그릴 수 있는 전체 canvas이다.
# 객체를 사용하는 것이 matplotlib의 더 많은 기능을 사용할 수 있다.
fig: Figure = plt.figure()

# Figure에 Axes가 포함되지 않으면 Figure가 출력이 안 된다.
ax: Axes = fig.add_subplot()

# 그려진 Figure를 화면에 보이기
plt.show()
plt.close(fig)

# ------------
# Line plot

# Figure를 생성할 때 크기를 지정할 수 있다. (인치 단위)
# Figure의 색상도 지정할 수 있다.
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

# Figure에 Axes가 포함되지 않으면 Figure 가 출력이 안 된다.
ax: Axes = fig.add_subplot()
ax.plot([2, 3, 1])
plt.show()
plt.close(fig)

# ----------
# Scatter plot
fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax: Axes = fig.add_subplot()
ax.scatter([2, 3, 1], [2, 3, 4])
plt.show()
plt.close(fig)
