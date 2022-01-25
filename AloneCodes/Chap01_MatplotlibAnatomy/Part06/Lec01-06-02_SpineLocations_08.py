# 연습문제 3
# 임의의 지점으로 축을 이동시킨다

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine

import numpy as np

x_data = np.random.normal(loc=5, scale=3, size=(500,))
y_data = np.random.normal(loc=3, scale=3, size=(500,))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 15))
ax.scatter(x_data, y_data)

ax.tick_params(labelsize=20, colors='red')

x_avg = np.average(x_data)
y_avg = np.average(y_data)
print(x_avg, y_avg)

# 지정한 지점으로 축 이동시키기
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right', 'top']:
        spine.set_visible(False)
    elif spine_loc in ['left']:
        spine.set_position(('data', x_avg))
        spine.set_color('red')
    elif spine_loc in ['bottom']:
        spine.set_position(('data', y_avg))
        spine.set_color('red')

fig.tight_layout()
fig.show()
