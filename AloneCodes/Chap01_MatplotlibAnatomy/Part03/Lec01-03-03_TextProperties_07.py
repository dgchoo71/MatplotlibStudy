# Text Properties와 Font Dictionary 사용하기
# text rotation

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

rotation_list = [0, 15, 30, 25, 60, 75, 90]

ax.set_xlim([0, len(rotation_list) + 3])
ax.set_ylim([0, len(rotation_list) + 3])
ax.grid(True)

# 문자열의 회전 중심은 문자열의 중앙이다.
for r_idx, rotation in enumerate(rotation_list):
    x = len(rotation_list) + 1 - r_idx
    y = r_idx + 1
    ax.text(x=x, y=y,
            ha='left', va='center',
            s=f'rotation={rotation}',
            fontsize=15,
            rotation=rotation,
            bbox={'fc': '0.9', 'pad': 0})
    ax.scatter(x, y, color='red', linewidths=5)

fig.show()
