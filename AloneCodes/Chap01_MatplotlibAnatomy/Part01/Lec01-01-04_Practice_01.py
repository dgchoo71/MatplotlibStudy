# 연습문제
# add_subplot, subplots, plt.subplot2grid 를 사용하여 동일한 형식의 Axes 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def draw_add_subplot():
    # add_subplot
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    ax1: Axes = fig.add_subplot(311)
    ax2: Axes = fig.add_subplot(312)
    ax3: Axes = fig.add_subplot(313)
    fig.show()
    

def draw_subplots():
    # subplots
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 7), facecolor='linen')
    fig.show()


def draw_subplot2grid():
    fig = plt.figure(figsize=(7, 7), facecolor='linen')
    
    ax1: Axes = plt.subplot2grid(shape=(3, 1), loc=(0, 0), fig=fig)
    ax2: Axes = plt.subplot2grid(shape=(3, 1), loc=(1, 0), fig=fig)
    ax3: Axes = plt.subplot2grid(shape=(3, 1), loc=(2, 0), fig=fig)
    fig.show()
    
    
if __name__ == '__main__':
    draw_add_subplot()
    draw_subplots()
    draw_subplot2grid()
    