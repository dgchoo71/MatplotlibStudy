# 축을 자유롭게 배치하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

# 전체 3 X 3 그리그의 위치에 축을 배치하기
ax1: Axes = plt.subplot2grid((3, 3), (0, 0), colspan=2, fig=fig)
ax2: Axes = plt.subplot2grid((3, 3), (1, 0), colspan=3, fig=fig)
ax3: Axes = plt.subplot2grid((3, 3), (2, 0), fig=fig)
ax4: Axes = plt.subplot2grid((3, 3), (2, 1), fig=fig)
ax5: Axes = plt.subplot2grid((3, 3), (2, 2), fig=fig)
fig.show()
