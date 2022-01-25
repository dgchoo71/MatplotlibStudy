# 세번째 연습문제

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw_add_subplot():
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    ax1: Axes = fig.add_subplot(1, 2, 1)
    ax2: Axes = fig.add_subplot(2, 2, 2, projection='3d')
    ax3: Axes = fig.add_subplot(2, 2, 4, projection='3d')
    fig.show()
    
    
def draw_subplot2grid():
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    ax1: Axes = plt.subplot2grid(shape=(2, 2), loc=(0, 0), rowspan=2, fig=fig)
    ax2: Axes = plt.subplot2grid(shape=(2, 2), loc=(0, 1), projection='3d', fig=fig)
    ax3: Axes = plt.subplot2grid(shape=(2, 2), loc=(1, 1), projection='3d', fig=fig)
    fig.show()
    
    
if __name__ == '__main__':
    draw_add_subplot()
    draw_subplot2grid()
    

