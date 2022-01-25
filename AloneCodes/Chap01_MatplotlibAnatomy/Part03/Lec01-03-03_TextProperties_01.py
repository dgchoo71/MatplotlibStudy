# Text Properties와 Font Dictionary 사용하기
# Fontsize

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

fontsize_list = [20, 30, 40]

ax.set_xlim([-1, 1])
ax.set_ylim([0, len(fontsize_list) + 1])

for font_idx, fontsize in enumerate(fontsize_list):
    ax.text(0, font_idx + 1, ha='center',
            s=f'fontsize={fontsize}',
            fontsize=fontsize)
    
fig.show()
