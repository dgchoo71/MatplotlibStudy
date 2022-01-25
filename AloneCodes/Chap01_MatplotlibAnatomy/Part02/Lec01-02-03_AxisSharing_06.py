# add_subplot을 이용하여 X, Y 축을 따로 공유하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure = plt.figure(figsize=(7, 7))

ax1_1: Axes = fig.add_subplot(221)
ax1_2: Axes = fig.add_subplot(222, sharey=ax1_1)

ax2_1: Axes = fig.add_subplot(223, sharex=ax1_1)
ax2_2: Axes = fig.add_subplot(224, sharex=ax1_2, sharey=ax2_1)

x1 = [-10, 10]
x2 = [0, 10]

y1 = [0, 100]
y2 = [0, 50]

# 기준이 되는 Axis에 축의 범위를 설정한다
# 기준이 되는 Axis는 subplot을 정의할 때 사용된 축의 이름이다.
ax1_1.set_ylim(y1)
ax1_1.set_xlim(x1)

ax1_2.set_xlim(x2)
ax2_1.set_ylim(y2)

fig.tight_layout()
fig.show()
