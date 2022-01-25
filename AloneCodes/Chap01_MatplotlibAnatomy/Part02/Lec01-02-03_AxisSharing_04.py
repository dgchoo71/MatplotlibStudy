# 축 공유하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np
import numpy.typing as npt

# X, Y 축을 공유하는 축들 생성
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7),
                         sharex=True, sharey=True)
fig: Figure = fig
axes: npt.NDArray[Axes] = axes

fig.subplots_adjust(bottom=0.05, top=0.95,
                    left=0.05, right=0.95, hspace=0.05)

axes[0, 0].set_xlim([10, 120])
axes[0, 0].set_ylim([0, 1])
fig.show()

