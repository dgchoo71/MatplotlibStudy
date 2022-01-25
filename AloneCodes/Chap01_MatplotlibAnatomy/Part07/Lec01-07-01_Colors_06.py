# discrete colormap 사용하기
# https://matplotlib.org/stable/tutorials/colors/colormaps.html

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from matplotlib.spines import Spine
import numpy as np

import matplotlib.cm as cm
from matplotlib.colors import ListedColormap


cmap: ListedColormap = cm.get_cmap('tab10')
n_color = len(cmap.colors)
print(cmap.colors)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, len(cmap.colors)])

# cmap은 ListColormap 클래스이다.
# 범위를 넘어서는 인덱스를 사용하면 마지막 color를 사용한다.
for c_idx in range(len(cmap.colors) + 1):
    color: tuple = cmap(c_idx)
    c_string_list = [c for c in str(color)]
    c_string = ''.join(c_string_list)
    
    ax.text(0, c_idx, f'color = {c_string}',
            fontsize=15, ha='center', color=color)
    
fig.show()

    
