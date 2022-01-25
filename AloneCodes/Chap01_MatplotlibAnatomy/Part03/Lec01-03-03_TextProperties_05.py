# Text Properties와 Font Dictionary 사용하기
# color

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

color_list = ['red', 'darkred', 'chocolate',
              'orange', 'olive', 'palegreen',
              'skyblue', 'navy', 'indigo']

ax.set_xlim([-1, 1])
ax.set_ylim([0, len(color_list) + 1])

for font_idx, color in enumerate(color_list):
    ax.text(0, font_idx + 1, ha='center',
            s=f'color={color}',
            fontsize=30, color=color)
    
fig.show()
