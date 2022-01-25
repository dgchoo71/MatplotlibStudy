# 연습문제 2
# 데이터가 0인 점을 기준으로 축을 이동한다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine

import numpy as np

np.random.seed(0)
t_min, t_max = -2, 10
n_data = 100

t = np.linspace(t_min, t_max, n_data)
noise_data = np.random.normal(0, 1, size=(n_data,))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))
ax.plot(t, noise_data)

fig.tight_layout()
ax.tick_params(labelsize=20)

# left, bottom의 축을 데이터가 0인 지점으로 이동시킨다.
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['top', 'right']:
        spine.set_visible(False)
    elif spine_loc in ['left', 'bottom']:
        spine.set_position('zero')
        # 또는
        spine.set_position(('data', 0))
        
fig.show()
