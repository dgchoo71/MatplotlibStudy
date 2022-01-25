# 넘파이 배열을 이용하여 Axis 생성하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import numpy.typing as npt


def draw1():
    # 일반적인 방법
    fig: Figure = plt.figure(figsize=(7, 7))
    
    ax1: Axes = fig.add_subplot(311)
    ax2: Axes = fig.add_subplot(312, sharex=ax1)
    ax3: Axes = fig.add_subplot(313, sharex=ax1)
    
    ax3.set_xlim([10, 100])
    fig.show()


def draw2():
    # 루프를 이용한 방법
    fig: Figure = plt.figure(figsize=(7, 7))
    axes: npt.NDArray[Axes] = np.empty(shape=(0,))
    
    for ax_idx in range(1, 1 + 3):
        if ax_idx == 1:
            axes = np.append(axes,
                             fig.add_subplot(3, 1, ax_idx))
        else:
            axes = np.append(axes,
                             fig.add_subplot(3, 1, ax_idx, sharex=axes[0]))
            
    axes[0].set_xlim([10, 100])
    
    
if __name__ == '__main__':
    draw1()
    draw2()

    

