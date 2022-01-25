# Text Properties와 Font Dictionary 사용하기
# Font Dictionary 없이 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

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

# Font Dictionary 없이 설정하기
ax.set_title('Random Data', fontsize=30, fontfamily='serif',
             color='darkblue', alpha=0.8, y=1.1)
ax.set_xlabel('Data Index', fontsize=20, color='darkblue', alpha=0.6)
ax.set_ylabel('Data Value', fontsize=20, color='darkblue', alpha=0.6)

ax.text(x=max_idx, y=max_val - 0.1,
        s=max_str, fontsize=15, color='red', va='top', ha='center',
        bbox={'boxstyle': 'Round', 'color': 'red', 'alpha': 0.3})

ax.text(x=min_idx, y=min_val + 0.1,
        s=min_str, fontsize=15, color='blue', va='bottom', ha='center',
        bbox={'boxstyle': 'Round', 'color': 'blue', 'alpha': 0.3})

# fig.tight_layout()
fig.subplots_adjust(top=0.8)
fig.show()

