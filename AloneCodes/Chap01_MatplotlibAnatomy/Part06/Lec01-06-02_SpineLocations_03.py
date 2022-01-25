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

# top과 right spine을 이용하기
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['left', 'bottom']:
        spine.set_visible(False)
    elif spine_loc in ['right']:
        spine.set_position('center')

ax.tick_params(labelsize=20,
               bottom=False, labelbottom=False,
               left=False, labelleft=False,
               right=True, labelright=True,
               top=True, labeltop=True)

fig.show()
