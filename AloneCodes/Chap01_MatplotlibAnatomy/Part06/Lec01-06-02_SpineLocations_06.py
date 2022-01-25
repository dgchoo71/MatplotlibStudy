# 연습문제 2
# 데이터가 0인 점을 기준으로 축을 이동한다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine

import numpy as np

t = np.linspace(-10, 9, 500)
sin = np.sin(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(20, 7))
ax.plot(t, sin)

fig.tight_layout()
ax.tick_params(labelsize=20)

# left, bottom spine을 가운데로 이동하기
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['top', 'right']:
        spine.set_visible(False)
    elif spine_loc in ['left', 'bottom']:
        spine.set_position('zero')
        # 또는
        spine.set_position(('data', 0))
        
fig.show()
