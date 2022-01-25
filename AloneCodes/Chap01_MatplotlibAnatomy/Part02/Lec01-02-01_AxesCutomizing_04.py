# Axis Layout Adjustment

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
fig: Figure = fig
axes: np.ndarray = axes

for ax_idx, ax in enumerate(axes.flat):
    ax: Axes = ax
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

fig.subplots_adjust(bottom=0.01, top=0.99, left=0.01, right=0.99)
fig.show()

fig.subplots_adjust(bottom=0.05, top=0.9, left=0.05, right=0.8)
fig.show()

