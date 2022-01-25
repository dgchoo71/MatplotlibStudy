# enumerate과 flat을 사용하여 subplots로 생성된 Axes 객체 다루기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy.typing as npt

# 축의 제목들
title_list = ["Training Image", "2 scales", "4 scales",
              "5 scales", "6 scales", "8 scales"]

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))

axes: npt.NDArray[Axes] = axes
for ax_idx, ax in enumerate(axes.flat):
    ax: Axes = ax
    ax.set_title(title_list[ax_idx], fontsize=20)
    
fig: Figure = fig
fig.show()
