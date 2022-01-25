# Axis Layout Adjustment

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(7, 7))
fig: Figure = fig
axes: np.ndarray = axes

for ax_idx, ax in enumerate(axes.flat):
    ax: Axes = ax
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

fig.subplots_adjust(hspace=0.2, wspace=0.05)
fig.show()


