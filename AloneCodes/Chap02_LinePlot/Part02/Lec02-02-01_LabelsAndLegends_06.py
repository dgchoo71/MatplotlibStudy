# Legend의 칼럼 개수 설정 (ncol)

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np

PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 300)
sin = np.sin(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

for ax_idx in range(12):
    label_template = 'added by {}'
    ax.plot(t, sin + ax_idx, label=label_template.format(ax_idx))

# legend를 아래쪽에 위치시킨다.
ax.legend(fontsize=15,
          ncol=4,
          bbox_to_anchor=(0.5, -0.05),
          loc='upper center')
fig.tight_layout()
fig.show()
