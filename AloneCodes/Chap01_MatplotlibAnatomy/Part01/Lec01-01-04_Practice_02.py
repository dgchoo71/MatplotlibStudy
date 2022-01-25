# 두번째 연습 문제

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw_add_subplot():
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    # row wise로 인덱스가 부여된다.
    ax1: Axes = fig.add_subplot(221)
    ax2: Axes = fig.add_subplot(222)
    ax3: Axes = fig.add_subplot(223)
    ax4: Axes = fig.add_subplot(224)
    fig.show()
    
    
def draw_subplots():
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7), facecolor='linen')
    fig.show()
    
    
def draw_subplot2grid():
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    ax1: Axes = plt.subplot2grid(shape=(2, 2), loc=(0, 0), fig=fig)
    ax2: Axes = plt.subplot2grid(shape=(2, 2), loc=(0, 1), fig=fig)
    ax3: Axes = plt.subplot2grid(shape=(2, 2), loc=(1, 0), fig=fig)
    ax4: Axes = plt.subplot2grid(shape=(2, 2), loc=(1, 1), fig=fig)
    fig.show()
    
    
if __name__ == '__main__':
    draw_add_subplot()
    draw_subplots()
    draw_subplot2grid()
    
    