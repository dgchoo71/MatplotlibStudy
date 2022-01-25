# tick label rotation
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html?highlight=tick_params#matplotlib.axes.Axes.tick_params


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

# 모든 tick label을 회전시킨다.
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20, length=10, width=3,
               rotation=30)
fig.show()

# -30도로 회전
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20, length=10, width=3,
               rotation=-30)
fig.show()


