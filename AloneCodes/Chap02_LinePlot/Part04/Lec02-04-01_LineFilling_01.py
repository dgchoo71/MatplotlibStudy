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
ax.axhline(0, color='red')

# X 축과 Sin 함수 사이의 영역에 색칠하기
ax.fill_between(t, sin)  # 첫번째 인자는 기준선이 된다.
fig.show()
