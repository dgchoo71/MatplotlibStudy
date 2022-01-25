# twinx 예제

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure()

ax1: Axes = fig.add_subplot()
ax2: Axes = ax1.twinx()

# X 축의 범위는 공유된다.
ax1.set_xlim([0, 100])

# Y 축의 범위 설정
ax1.set_ylim([0, 100])
ax2.set_ylim([0, 0.1])

# 축의 타이틀 설정
ax1.set_title("Twinx Graph", fontsize=20)
ax1.set_xlabel("Time (sec)", fontsize=15)
ax1.set_ylabel("Data1", fontsize=15)
ax2.set_ylabel("Data2", fontsize=15)

fig.tight_layout()
fig.show()
