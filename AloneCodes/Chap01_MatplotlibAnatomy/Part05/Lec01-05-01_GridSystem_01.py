# Grid
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html?highlight=grid#matplotlib.axes.Axes.grid

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure
ax: Axes

# 기본적은 그리드 표시
fig, ax = plt.subplots(figsize=(7, 7))
ax.grid()
fig.show()
plt.close(fig)

# X 축에 그리드 표시
fig, ax = plt.subplots(figsize=(7, 7))
ax.grid(axis='x')
fig.show()
plt.close(fig)

# Y 축에 그리드 표시
fig, ax = plt.subplots(figsize=(7, 7))
ax.grid(axis='y')
fig.show()
plt.close(fig)
