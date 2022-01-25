# 축별 설정
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html?highlight=tick_params#matplotlib.axes.Axes.tick_params


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

# x 축의 tick만 변경하기
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(axis='x',
               labelsize=20, length=10, width=3,
               rotation=30)
fig.show()

# y 축의 tick만 변경하기
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(axis='y',
               labelsize=20, length=10, width=3,
               rotation=30)
fig.show()

