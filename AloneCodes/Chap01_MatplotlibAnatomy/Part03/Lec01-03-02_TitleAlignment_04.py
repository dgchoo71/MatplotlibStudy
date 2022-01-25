# Figure의 타이틀 위치 설정하기
# 음수의 Y 값도 사용 가능하다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw1():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    # 축의 타이틀을 맨 위에 위치시킨다.
    ax.set_title('Ax Title', fontsize=20, y=-0.05)
    ax.set_ylim([0, 10])
    
    fig.show()


def draw2():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    # 축의 타이틀을 중간에 위치시킨다
    ax.set_title('Ax Title', fontsize=20, y=-0.1)
    
    # 축의 범위와는 관계가 없다
    ax.set_ylim([0, 10])
    
    fig.show()


def draw3():
    figsize = (7, 7)
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=figsize)
    
    # 축의 타이틀을 아래에 위치시킨다
    ax.set_title('Ax Title', fontsize=20, y=-0.15)
    ax.set_ylim([0, 10])
    
    fig.show()


if __name__ == '__main__':
    draw1()
    draw2()
    draw3()

    
