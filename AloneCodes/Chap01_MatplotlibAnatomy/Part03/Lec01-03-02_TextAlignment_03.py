# Text Alignment 위치 이동하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import typing


def draw_grid() -> typing.Union[Figure, Axes]:
    figsize = (7, 7)
    fig: Figure; ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    
    ax.grid()
    ax.tick_params(axis='both', labelsize=15)

    return fig, ax
    
    
def draw_text_ha():
    fig: Figure; ax: Axes
    fig, ax = draw_grid()

    ax.set_title('Horizontal Text Alignment', fontsize=30)
    
    # 기준점으로 Text Alignment 맞추기
    x, y = -0.75, -0.5
    ax.scatter(x, y, color='black', linewidths=5)
    ax.text(x=x, y=y, s='va=center, ha=left',
            va='center', ha='left', fontsize=30)

    x, y = 0, 0
    ax.scatter(x, y, color='black', linewidths=5)
    ax.text(x=x, y=y, s='va=center, ha=center',
            va='center', ha='center', fontsize=30)

    x, y = 0.75, 0.5
    ax.scatter(x, y, color='black', linewidths=5)
    ax.text(x=x, y=y, s='va=center, ha=right',
            va='center', ha='right', fontsize=30)
    
    fig.show()


def draw_text_va():
    fig: Figure; ax: Axes
    fig, ax = draw_grid()

    ax.set_title('Vertial Text Alignment', fontsize=30)

    # 기준점으로 Text Alignment 맞추기
    x, y = 0, 0.5
    ax.scatter(x, y, color='black', linewidths=5)
    ax.text(x=x, y=y, s='va=top, ha=center',
            va='top', ha='center', fontsize=30)

    x, y = 0, 0
    ax.scatter(x, y, color='black', linewidths=5)
    ax.text(x=x, y=y, s='va=center, ha=center',
            va='center', ha='center', fontsize=30)

    x, y = 0, -0.5
    ax.scatter(x, y, color='black', linewidths=5)
    ax.text(x=x, y=y, s='va=bottom, ha=center',
            va='bottom', ha='center', fontsize=30)

    fig.show()


if __name__ == '__main__':
    draw_text_ha()
    draw_text_va()