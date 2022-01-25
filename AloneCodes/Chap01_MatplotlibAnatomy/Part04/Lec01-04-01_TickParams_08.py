# 일정한 간격으로 x tick의 값을 설정하기
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(10, 10))

# 20 간격으로 tick 값을 생성
xticks = [i for i in range(0, 101, 20)]
ax.set_xticks(xticks)  # x축의 tick을 설정
ax.tick_params(axis='x', labelsize=20, length=10,
               width=3, rotation=30)
fig.show()
