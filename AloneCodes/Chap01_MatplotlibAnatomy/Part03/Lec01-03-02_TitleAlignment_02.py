# Figure와 축의 타이틀 위치 설정하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw1():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    title_bottom = 0.9
    
    # Figure의 타이틀과 ax의 타이틀이 겹쳐기제 된다.
    fig.suptitle('Title', fontsize=30, y=title_bottom, va='bottom')
    ax.set_title('Ax Title', fontsize=20)
    
    fig.subplots_adjust(top=title_bottom)
    fig.show()


def draw2():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    title_bottom = 0.9
    
    fig.suptitle('Title', fontsize=30, y=title_bottom, va='bottom')
    ax.set_title('Ax Title', fontsize=20)
    
    # Figure의 크기를 조정하여 Figure의 타이틀과 차트 영역의 타이틀이 겹치는 것을 막는다.
    fig.subplots_adjust(top=title_bottom - 0.1)
    
    fig.show()


if __name__ == '__main__':
    draw1()
    draw2()

    
