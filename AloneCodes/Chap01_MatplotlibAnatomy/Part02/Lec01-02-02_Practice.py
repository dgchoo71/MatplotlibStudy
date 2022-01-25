# Axis Layout Adjustment 연습 문제

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure(figsize=(12, 13))
axes: np.ndarray = np.empty(shape=(0, 7))

for grp_idx in range(2):
    axes_grp: np.ndarray = np.empty(shape=(0,))
    main = plt.subplot2grid(shape=(5, 4), loc=(0, 2 * grp_idx),
                            rowspan=2, colspan=2, fig=fig)
    
    axes_grp = np.append(main, axes_grp)
    
    for r_idx in range(2, 2 + 3):
        for c_idx in range(2):
            ax: Axes = plt.subplot2grid(shape=(5, 4),
                                        loc=(r_idx, c_idx + 2 * grp_idx),
                                        fig=fig)
            axes_grp = np.append(axes_grp, ax)
            
    axes_grp = axes_grp.reshape(1, -1)
    axes: np.ndarray = np.vstack((axes, axes_grp))
    
for ax_idx, ax in enumerate(axes.flat):
    ax: Axes = ax
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
fig.subplots_adjust(bottom=0.03, top=0.97, left=0.03, right=0.97,
                    hspace=0, wspace=0)
    
fig.show()
