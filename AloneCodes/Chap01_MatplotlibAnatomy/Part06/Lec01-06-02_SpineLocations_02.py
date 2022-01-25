# Spine의 위치를 이동할 수 있다.
# spine.set_position

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine

import numpy as np

fig: Figure
ax: Axes
fig, ax = plt.subplots()

spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right', 'top']:
        # 불필요한 spine을 제거
        spine.set_visible(False)
    elif spine_loc in ['left', 'bottom']:
        # left와 bottom 축을 가운데로 이동
        spine.set_position('center')

fig.show()
