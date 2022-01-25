# logit scale 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


logit = np.linspace(-10, 10, 300)
sigmoid = 1 / (1 + np.exp(-logit))


def draw1():
    # Sigmoid
    fig: Figure = plt.figure()
    ax: Axes = fig.add_subplot()
    ax.plot(logit, sigmoid)
    fig.show()
    

def draw2():
    # sigmoid 함수에 logit scale 적용하기
    
    fig: Figure = plt.figure()
    ax: Axes = fig.add_subplot()

    # logit의 역함수가 sigmoid이다
    # 따라서, logit scale을 사용하면 logit 함수의 역함수인 sigmoid 함수를 linear하게 표현한다.
    # 즉, 선형으로 표현하고 싶은 함수의 역함수를 scale로 설정한다.
    ax.set_yscale('logit')
    
    ax.plot(logit, sigmoid)
    fig.show()

    
if __name__ == '__main__':
    draw1()
    draw2()
    