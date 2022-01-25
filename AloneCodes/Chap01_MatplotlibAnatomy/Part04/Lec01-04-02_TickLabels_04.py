# Tick Labels 연습문제 3

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine

import numpy as np


fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(10, 10))

ax.set_xscale('log')
ax.set_yscale('log')

major_xticks = [10 ** i for i in range(5)]
major_yticks = [1E-10, 1E-5, 1E0]

# Y 축의 Minor tick을 linear하게 표현
minor_yticks = [10 ** i for i in range(-10, 4)]

ax.set_xticks(major_xticks)
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)

ax.tick_params(which='major', direction='in', length=8, labelsize=20)
ax.tick_params(which='minor', direction='in', length=5, labelsize=0)

# grid 표시
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right', 'top']:
        spine.set_visible(False)
        
ax.grid(which='major', color='silver')
ax.grid(which='minor', linestyle=':', color='silver')

fig.show()
