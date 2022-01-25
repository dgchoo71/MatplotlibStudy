# 연습문제 1

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine

import numpy as np

noise_data = np.random.normal(0, 1, (100,))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(noise_data)

fig.tight_layout()
ax.tick_params(labelsize=15)

# bottom spine을 가운데로 이동하기
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['top', 'right']:
        spine.set_visible(False)
    elif spine_loc in ['bottom']:
        spine.set_position('center')
        
    if spine_loc in ['left', 'bottom']:
        spine.set_color('navy')
        spine.set_linewidth(2)

# bottom 축은 중앙으로 이동했지만, 정확하게 y값이 0인 위치에 맞지는 않다.
fig.show()
