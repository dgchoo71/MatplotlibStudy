# Axes.set_xticks : x 축의 tick 위치와 minor tick에 대한 설정
# Axes.set_yticks : y 축의 tick 위치와 minor tick에 대한 설정
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(10, 10))

# x축의 원하는 곳에 tick label들을 설정
xticks = [i for i in range(11)]
ax.set_xticks(xticks)
ax.tick_params(labelsize=20)

fig.show()

