# Title, label and Font Dict 연습 문제 1

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


title_list = ['Training Image', '2 scale', '4 scale',
              '5 scale', '6 scale', '8 scale']

title_font_dict = dict(fontsize=20, fontweight='bold')

fig: Figure
axes: np.ndarray
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))

ax_idx: int
ax: Axes
for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(title_list[ax_idx], fontdict=title_font_dict)
    
    # 차트의 축을 없앤다.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    
fig.tight_layout()
fig.show()

