# major, minor tick 설정
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html?highlight=tick_params#matplotlib.axes.Axes.tick_params
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(14, 7))

# major tick 설정
major_xticks = [i for i in range(0, 101, 20)]
ax.set_xticks(major_xticks)
ax.tick_params(axis='x', labelsize=20, length=10, width=3, rotation=30)

# minor tick 설정
# major tick을 4 등분하는 minor tick을 생성한다.
minor_xticks = [i for i in range(0, 101, 5)]
ax.set_xticks(minor_xticks, minor=True)
ax.tick_params(axis='x', which='minor', length=5, width=2)

fig.show()

