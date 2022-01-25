# 하나의 차트에서 동일한 X 축을 공유 (Y 축은 다를 경우)
# 다른 그래프를 하나의 차트에 그릴 때 사용

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


def draw1():
    # Y 축이 다른 그래프를 하나의 차트에 그릴 때
    # dimension의 차이가 심하다.
    t = np.linspace(0.01, 5 * np.pi, 100)
    sin = np.sin(t)
    exp = np.exp(t)
    
    fig: Figure = plt.figure(figsize=(7, 7))
    ax1: Axes = fig.add_subplot()
    
    ax1.plot(t, sin)
    ax1.plot(t, exp)
    
    fig.show()
    

def draw2():
    # twinx 를 이용하여 새로운 축을 생성
    # 두 개의 그래프를 겹쳐서 그려도 전혀 다른 차트 객체이다.
    t = np.linspace(0.01, 5 * np.pi, 100)
    sin = np.sin(t)
    exp = np.exp(t)

    fig: Figure = plt.figure(figsize=(7, 7))
    ax1: Axes = fig.add_subplot()
    ax1.plot(t, sin)
    
    # 첫번째 차트의 X 축을 공유하는 새로운 차트를 생성
    ax2: Axes = ax1.twinx()
    ax2.plot(t, exp)
    
    fig.show()
    

if __name__ == '__main__':
    draw1()
    draw2()
    
    
    