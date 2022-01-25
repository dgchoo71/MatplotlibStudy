# 축의 레이블을 변경한다.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html

# Axes.set_xticks를 설정하고 난 뒤, Axes.set_xticklabels를 설정해야 한다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

xticks = [i for i in range(10)]
xtick_labels = [f'Class {i}' for i in xticks]

yticks = [i for i in range(0, 101, 20)]
ytick_labels = [f'{i} %' for i in yticks]

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xticks(xticks)       # tick의 위치를 먼저 설정한다
ax.set_xticklabels(xtick_labels)  # tick의 값을 설정

ax.set_yticks(yticks)
ax.set_yticklabels(ytick_labels)

# 축의 서식 설정
ax.tick_params(labelsize=20, labelrotation=60)
ax.tick_params(axis='y', labelrotation=0)   # y축의 레이블은 회전하지 않는다.

fig.subplots_adjust(bottom=0.2, left=0.15)
fig.show()
