# Text Properties와 Font Dictionary 사용하기
# alpha

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

alpha_list = [0.1, 0.3, 0.5, 0.7, 0.9, 1]

ax.set_xlim([-1, 1])
ax.set_ylim([0, len(alpha_list) + 1])

for font_idx, alpha in enumerate(alpha_list):
    ax.text(0, font_idx + 1, ha='center',
            s=f'alpha={alpha}',
            fontsize=30, alpha=alpha)
    
fig.show()
