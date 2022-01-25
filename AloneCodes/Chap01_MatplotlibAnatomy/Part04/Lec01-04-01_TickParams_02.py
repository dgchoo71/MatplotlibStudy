# Tick과 Tick Label 설정하기
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html?highlight=tick_params#matplotlib.axes.Axes.tick_params


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

# bottom의 tick은 없애고 top의 tick은 보이도록 설정
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20, length=10, width=3,
               bottom=False, labelbottom=False,
               top=True, labeltop=True)
fig.show()

# top과 right의 tick을 보이도록 설정
# 기본은 left, bottom이므로 False로 설정해야 한다.
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20, length=10, width=3,
               bottom=False, labelbottom=False,
               left=False, labelleft=False,
               top=True, labeltop=True,
               right=True, labelright=True)
fig.show()
