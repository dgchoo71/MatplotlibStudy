# x축과 y축의 major, minor tick 설정
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html?highlight=tick_params#matplotlib.axes.Axes.tick_params
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(14, 7))

major_xticks = [i for i in range(0, 101, 20)]
minor_xticks = [i for i in range(0, 101, 5)]
major_yticks = [i for i in range(0, 11, 2)]
minor_yticks = [i for i in range(0, 11, 1)]

# x축의 tick 설정
ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)
ax.tick_params(axis='x', labelsize=20, length=10, width=3, rotation=30)
ax.tick_params(axis='x', which='minor', length=5, width=2)

# y축의 tick 설정
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)
ax.tick_params(axis='y', labelsize=20, length=10, width=3)
ax.tick_params(axis='y', which='minor', length=5, width=2)

fig.show()

