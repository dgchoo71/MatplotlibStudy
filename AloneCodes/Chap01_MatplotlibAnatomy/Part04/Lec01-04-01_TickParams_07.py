# 임의의 x tick 값을 설정하기
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(10, 10))

# x축의 원하는 곳에 tick label들을 설정
ax.set_xticks([0, 1, 5, 10])
ax.tick_params(labelsize=20)

fig.show()

