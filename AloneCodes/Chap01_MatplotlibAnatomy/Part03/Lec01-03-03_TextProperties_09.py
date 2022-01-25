# Text Properties와 Font Dictionary 사용하기
# Font Dictionary 사용하기
# 수정에 유리하다

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

# region: define font dictionary
title_font_dict = dict(fontsize=30, fontfamily='serif',
                       color='darkblue', alpha=0.8)

xylabel_fint_dict = dict(fontsize=20, color='darkblue', alpha=0.6)

max_font_dict = dict(fontsize=15, color='red', va='top', ha='center',
                     bbox={'boxstyle': 'Round', 'color': 'red', 'alpha': 0.3})

min_font_dict = dict(fontsize=15, color='blue', va='bottom', ha='center',
                     bbox={'boxstyle': 'Round', 'color': 'blue', 'alpha': 0.3})
# endregion

figsize = (7, 7)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=figsize)

data = np.random.normal(loc=0, scale=1, size=(10,))

max_idx, max_val = np.argmax(data), np.round(np.max(data), 2)
min_idx, min_val = np.argmin(data), np.round(np.min(data), 2)

max_str = f'Max: ({max_idx}, {max_val})'
min_str = f'Min: ({min_idx}, {min_val})'

ax.plot(data)

# region: Font Dictionary 사용하기
ax.set_title('Random Data', y=1.1, fontdict=title_font_dict)
ax.set_xlabel('Data Index', fontdict=xylabel_fint_dict)
ax.set_ylabel('Data Value', fontdict=xylabel_fint_dict)

ax.text(x=max_idx, y=max_val - 0.1, s=max_str, fontdict=max_font_dict)
ax.text(x=min_idx, y=min_val + 0.1, s=min_str, fontdict=min_font_dict)
# endregion

fig.subplots_adjust(top=0.8)
fig.show()
