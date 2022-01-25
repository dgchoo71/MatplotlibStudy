# Text Properties와 Font Dictionary 사용하기
# Fontweight

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

fontweight_list = ['ultralight', 'light', 'normal', 'regular',
                   'book', 'medium', 'roman', 'semibold',
                   'demibold', 'demi', 'bold', 'heavy',
                   'extra bold', 'black']

ax.set_xlim([-1, 1])
ax.set_ylim([0, len(fontweight_list) + 1])

for font_idx, fontweight in enumerate(fontweight_list):
    ax.text(0, font_idx + 1, ha='center',
            s=f'fontweight={fontweight}',
            fontsize=20, fontweight=fontweight)
    
fig.show()
