# 네번째 연습문제

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw_subplot2grid():
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    ax1: Axes = plt.subplot2grid(shape=(5, 4), loc=(0, 0), rowspan=2, colspan=2, fig=fig)
    ax2: Axes = plt.subplot2grid(shape=(5, 4), loc=(0, 2), rowspan=2, colspan=2, fig=fig)
    
    ax3: Axes = plt.subplot2grid(shape=(5, 4), loc=(2, 0), fig=fig)
    ax4: Axes = plt.subplot2grid(shape=(5, 4), loc=(2, 1), fig=fig)
    ax5: Axes = plt.subplot2grid(shape=(5, 4), loc=(2, 2), fig=fig)
    ax6: Axes = plt.subplot2grid(shape=(5, 4), loc=(2, 3), fig=fig)
    
    ax7: Axes = plt.subplot2grid(shape=(5, 4), loc=(3, 0), fig=fig)
    ax8: Axes = plt.subplot2grid(shape=(5, 4), loc=(3, 1), fig=fig)
    ax9: Axes = plt.subplot2grid(shape=(5, 4), loc=(3, 2), fig=fig)
    ax10: Axes = plt.subplot2grid(shape=(5, 4), loc=(3, 3), fig=fig)

    ax11: Axes = plt.subplot2grid(shape=(5, 4), loc=(4, 0), fig=fig)
    ax12: Axes = plt.subplot2grid(shape=(5, 4), loc=(4, 1), fig=fig)
    ax13: Axes = plt.subplot2grid(shape=(5, 4), loc=(4, 2), fig=fig)
    ax14: Axes = plt.subplot2grid(shape=(5, 4), loc=(4, 3), fig=fig)
    
    fig.show()


def draw_subplot2grid_loop():
    # 루프를 이용하여 axes를 생성
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    # 빈 배열 선언
    axes: np.ndarray = np.empty(shape=(0,))
    
    axes = np.append(axes, plt.subplot2grid(shape=(5, 4), loc=(0, 0), rowspan=2, colspan=2, fig=fig))
    axes = np.append(axes, plt.subplot2grid(shape=(5, 4), loc=(0, 2), rowspan=2, colspan=2, fig=fig))
    
    for r_idx in range(2, 5):
        for c_idx in range(4):
            axes = np.append(axes, plt.subplot2grid(shape=(5, 4), loc=(r_idx, c_idx), fig=fig))
            
    fig.show()
    
    
if __name__ == '__main__':
    draw_subplot2grid()
    draw_subplot2grid_loop()
    