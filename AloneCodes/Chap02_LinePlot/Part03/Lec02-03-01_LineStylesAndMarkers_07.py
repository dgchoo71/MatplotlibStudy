# Line Marker와 Legend 추가하가
# Legend에도 Marker가 표시된다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 50)
sin = np.sin(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin, label='$sin(t)$')

ax.plot(t, sin + 1,
        marker='o', label='$sin(t) + 1$')

ax.plot(t, sin + 2,
        marker='D', label='$sin(t) + 2$')

ax.plot(t, sin + 3,
        marker='s', label='$sin(t) + 3$')

ax.legend(loc='center left',
          bbox_to_anchor=(1, 0.5),
          fontsize=20)

fig.tight_layout()
fig.show()
