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
ax.fill_between(t, y1=sin, y2=cos, alpha=0.3)
fig.show()
