# Text Properties와 Font Dictionary 사용하기
# Fontfamily

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

fontfamily_list = ['serif', 'sans-serif', 'cursive',
                   'fantasy', 'monospace']

ax.set_xlim([-1, 1])
ax.set_ylim([0, len(fontfamily_list) + 1])

for font_idx, fontfamily in enumerate(fontfamily_list):
    ax.text(0, font_idx + 1, ha='center',
            s=f'fontfamily={fontfamily}',
            fontsize=30,
            fontfamily=fontfamily)
    
fig.show()
