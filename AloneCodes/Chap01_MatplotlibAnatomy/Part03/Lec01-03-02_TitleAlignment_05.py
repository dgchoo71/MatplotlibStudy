# 타이틀과 레이블의 텍스트에 대한 연습 문제

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


ax_title_list = ['(a) CE - clean', '(b) CE - noisy',
                 '(c) LSR - noisy', '(d) SL - noisy']

title_bottom = 0.9

fig: Figure
axes: np.ndarray

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

fig.suptitle('Symmetric Cross Entropy',
             fontsize=30,
             y=title_bottom + 0.03, va='bottom')

for ax_idx, ax in enumerate(axes.flat):
    ax: Axes = ax
    ax.set_title(label=ax_title_list[ax_idx],
                 fontsize=20,
                 y=-0.25)
    
    ax.set_xlabel('Number of epochs', fontsize=15)
    ax.set_ylabel('Class-wise test accuracy', fontsize=15)

fig.subplots_adjust(top=title_bottom, bottom=0.1,
                    hspace=0.3, wspace=0.3)
fig.show()
