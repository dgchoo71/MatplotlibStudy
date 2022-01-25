# 두 함수 사이의 색칠하기


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 200)
sin = np.sin(t)
cos = np.cos(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin, color='r')
ax.plot(t, cos, color='r')

# 두 함수 사이의 영역을 칠하기
# 두 함수의 차이값에 따라 다른 색을 사용
ax.fill_between(t, y1=sin, y2=cos,
                color='darkblue',
                alpha=0.3,
                where=sin>=cos)

ax.fill_between(t, y1=sin, y2=cos,
                color='darkred',
                alpha=0.3,
                where=sin<cos)
fig.show()
