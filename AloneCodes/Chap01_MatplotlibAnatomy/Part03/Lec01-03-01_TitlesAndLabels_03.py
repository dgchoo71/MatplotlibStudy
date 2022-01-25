# axes label

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


figsize = (7, 7)
fig, ax = plt.subplots(figsize=figsize)
fig: Figure = fig
ax: Axes = ax

fig.suptitle("Title of a Figure", fontsize=30,
             color="darkblue", alpha=0.9)

ax.set_xlabel("X Label", fontsize=20,
              color="darkblue", alpha=0.7)
ax.set_ylabel("Y Label", fontsize=20,
              color="darkblue", alpha=0.7)

fig.show()
