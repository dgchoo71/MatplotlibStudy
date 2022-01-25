# 축의 크기를 계산하여 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

left_margin, bottom_margin = 0.1, 0.1
right_margin, top_margin = 0.1, 0.1
spacing = 0.1


def draw_axes(width, height):
    rect1 = [left_margin, bottom_margin, width, height]
    rect2 = [left_margin + width + spacing, bottom_margin,
             1 - (left_margin + width + spacing + right_margin), height]
    rect3 = [left_margin, bottom_margin + height + spacing,
             1 - (left_margin + right_margin),
             1 - (bottom_margin + height + spacing + top_margin)]
    
    fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')
    
    ax1: Axes = fig.add_axes(rect1)
    ax2: Axes = fig.add_axes(rect2)
    ax3: Axes = fig.add_axes(rect3)

    fig.show()
    
    
if __name__ == '__main__':
    draw_axes(width=0.5, height=0.5)
    draw_axes(width=0.6, height=0.3)
    draw_axes(width=0.2, height=0.6)
