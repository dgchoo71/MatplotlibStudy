# Text Alignment

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
    
    
def draw_text():
    fig: Figure; ax: Axes
    fig, ax = draw_grid()
    
    ax.text(x=0, y=0, s="Hello1", fontsize=30)
    ax.text(x=0.5, y=0, s="Hello2", fontsize=30)
    ax.text(x=0.5, y=-0.5, s="Hello3", fontsize=30)

    fig.show()


if __name__ == '__main__':
    draw_text()