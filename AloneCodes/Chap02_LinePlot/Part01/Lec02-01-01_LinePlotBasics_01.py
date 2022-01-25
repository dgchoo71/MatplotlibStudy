# 하나의 데이터만 이용하여 Line Plot을 그릴 수 있다.
# 데이터는 Y값이 되며, X값은 인덱스이다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


np.random.seed(0)

y_data = np.random.normal(loc=0, scale=1, size=(100,))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(y_data)   # X값은 자동으로 데이터의 인덱스를 사용한다.

fig.tight_layout(pad=3)
ax.tick_params(labelsize=20)

fig.show()

# -----
# Spine을 변경
ax.grid()
spine: Spine
for spine_loc, spine in ax.spines.items():
    spine.set_linewidth(3)
    
    if spine_loc in ['right', 'top']:
        spine.set_visible(False)
        
    if spine_loc in ['bottom', 'left']:
        spine.set_position(('data', 0))

fig.show()

plt.close(fig)

