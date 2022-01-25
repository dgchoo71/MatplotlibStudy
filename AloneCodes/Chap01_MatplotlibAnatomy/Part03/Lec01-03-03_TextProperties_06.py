# Text Properties와 Font Dictionary 사용하기
# bbox
# https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

bbox_list = [
    {'boxstyle': 'DArrow', 'color': 'red', 'alpha': 0.5},
    {'boxstyle': 'Round', 'color': 'orange', 'alpha': 0.5},
    {'boxstyle': 'Sawtooth', 'color': 'red', 'alpha': 0.5},
    {'boxstyle': 'Square', 'color': 'navy', 'alpha': 0.5}
]

ax.set_xlim([-5, 5])
ax.set_ylim([0, len(bbox_list) + 1])

for b_idx, bbox in enumerate(bbox_list):
    ax.text(0, b_idx + 1, ha='center',
            s=bbox, fontsize=15, bbox=bbox)
    
fig.show()
