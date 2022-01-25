# Figure title, axes title, axes label

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw1():
    # Figure에 타이틀 설정하기

    fig: Figure = plt.figure()
    ax: Axes = fig.add_subplot()
    
    # Figure 자체의 타이틀 설정
    fig.suptitle("Title of Figure", fontsize=30,
                 fontfamily="monospace")
    
    plt.show()
    plt.close(fig)
   

def draw2():
    # 차트 영역에 타이틀 설정하기

    fig: Figure = plt.figure()
    ax: Axes = fig.add_subplot()

    ax.set_title("Tile of a Ax", fontsize=30,
                 fontfamily="monospace")

    plt.show()
    plt.close(fig)
    


if __name__ == '__main__':
    draw1()
    draw2()
