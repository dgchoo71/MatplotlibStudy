# Line Marker 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 300)
sin = np.sin(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin, color='black')

# 원(circle) 모양의 마커
ax.plot(t, sin + 1, marker='o', color='black')

# 다이어몬드(diamont) 모양의 마커
ax.plot(t, sin + 2, marker='D', color='black')

# 사각형(squar) 모양의 마커
ax.plot(t, sin + 3, marker='s', color='black')

fig.show()
