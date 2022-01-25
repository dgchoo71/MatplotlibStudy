# Figure의 타이틀 위치 설정하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw1():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    title_bottom = 0.9
    
    fig.suptitle('Title', fontsize=30, y=title_bottom, va='bottom')
    
    # figure의 크기를 조절하지 않으면 Figure의 타이틀과 차트 영역이 겹쳐지게 된다.
    fig.subplots_adjust(top=title_bottom)
    fig.show()


def draw2():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    title_bottom = 0.8
    
    fig.suptitle('Title', fontsize=30, y=title_bottom, va='bottom')
    
    fig.subplots_adjust(top=title_bottom)
    fig.show()


def draw3():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    title_bottom = 0.7
    
    fig.suptitle('Title', fontsize=30, y=title_bottom, va='bottom')
    
    fig.subplots_adjust(top=title_bottom)
    fig.show()


if __name__ == '__main__':
    draw1()
    draw2()
    draw3()
    
