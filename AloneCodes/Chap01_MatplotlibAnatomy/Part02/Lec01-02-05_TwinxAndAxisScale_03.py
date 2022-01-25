# 축의 scale 설정하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


def draw1():
    # scale을 설정하지 않은 경우
    t = np.linspace(0, 3, 300)
    exp = np.exp(t)
    
    fig: Figure = plt.figure()
    ax: Axes = fig.add_subplot()
    
    ax.plot(t, exp)
    
    fig.show()
    
    
def draw2():
    # Y 축의 scale을 설정한 경우
    t = np.linspace(0, 3, 300)
    exp = np.exp(t)

    fig: Figure = plt.figure()
    ax: Axes = fig.add_subplot()

    # log scale의 의미는 log 함수의 역함수인 exp 함수를 linear 하게 만드는 역할을 한다.
    # 따라서, exp 함수에 log scale을 지정하면 직선의 형태로 그래프가 그려진다.
    ax.set_yscale('log')
    ax.plot(t, exp)

    fig.show()


if __name__ == '__main__':
    draw1()
    draw2()
