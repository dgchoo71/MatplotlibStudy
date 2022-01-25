# continuous colormap 사용하기
# https://matplotlib.org/stable/tutorials/colors/colormaps.html

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from matplotlib.spines import Spine
import numpy as np

import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap

n_color = 10   # 연속된 colormap 중에 몇 개를 사용할 것인가
cmap: LinearSegmentedColormap = cm.get_cmap('rainbow', lut=n_color)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, cmap.N])

# cmap은 ListColormap 클래스이다.
for c_idx in range(cmap.N):
    color: tuple = cmap(c_idx)
    c_string_list = [c for c in str(color)]
    c_string = ''.join(c_string_list)
    
    ax.text(0, c_idx, f'color = {c_string}',
            fontsize=15, ha='center', color=color)
    
fig.show()

    
