# subplot2grid 로 생성한 축들의 공유

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure(figsize=(7, 7))

ax1: Axes = plt.subplot2grid(shape=(2, 3), loc=(0, 0), colspan=3, fig=fig)
ax2: Axes = plt.subplot2grid(shape=(2, 3), loc=(1, 0), colspan=2, fig=fig,
                             sharex=ax1)
ax3: Axes = plt.subplot2grid(shape=(2, 3), loc=(1, 2), fig=fig,
                             sharex=ax1)

ax1.set_xlim([0, 100])
fig.tight_layout()
fig.show()
