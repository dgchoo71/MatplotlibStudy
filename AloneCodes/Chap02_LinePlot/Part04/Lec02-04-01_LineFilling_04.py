# 두 함수 사이의 색칠하기


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 200)
sin = np.sin(t)


fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin, color='black')
ax.axhline(0, color='black')

# 색을 칠할 영역을 설정할 수 있다.
# sin이 0보다 크거나 같은 영역만 색을 칠하도록 설정
ax.fill_between(t, sin, alpha=0.3,
                where=sin>=0)

# sin이 0보다 작은 영역만 색을 칠한다.
ax.fill_between(t, sin, alpha=0.3,
                color='darkred',
                where=sin<0)

fig.show()
