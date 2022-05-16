# 데이터의 크기만을 표시하도록 범례를 출력
# 즉, 빈 차트에 범례만 표시한다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

legend_sizes = np.array([10, 20, 30, 40, 50])

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

for legend_size in legend_sizes:
    ax.scatter([], [],
               s=legend_size ** 2,
               c='tab:blue',
               label=f'{legend_size}')

ax.legend(loc='center left',
          bbox_to_anchor=(1, 0.5),
          title='Point size',
          title_fontsize=30,
          fontsize=30,
          labelspacing=1)

fig.tight_layout()
plt.show()
