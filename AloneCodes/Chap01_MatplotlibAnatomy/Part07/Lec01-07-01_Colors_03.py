# Named Colors (css color)
# 색상의 이름을 직접 지정 가능

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


title_font_dict = dict(fontsize=30, color='darkblue')
label_font_dict = dict(fontsize=20, color='darkblue', alpha=0.8)

fig: Figure = plt.figure(figsize=(7, 7), facecolor='powderblue')
ax: Axes = fig.add_subplot(facecolor='powderblue')

ax.set_title("Fig Title", fontdict=title_font_dict)
ax.set_xlabel("Data Index", fontdict=label_font_dict)
ax.set_ylabel("Data Value", fontdict=label_font_dict)

ax.tick_params(labelsize=15, colors='darkblue')

spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['left', 'bottom']:
        spine.set_color('darkblue')
    elif spine_loc in ['right', 'top']:
        spine.set_visible(False)
        
    if spine_loc in ['bottom']:
        spine.set_position(('data', 0))
        
test_np = np.random.normal(loc=0, scale=1, size=(10,))
ax.plot(test_np)    # tableau의 첫번째 색상인 tab:blue가 사용된다.

fig.tight_layout()
fig.show()
