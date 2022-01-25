# Tick과 Tick Label 설정하기
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html?highlight=tick_params#matplotlib.axes.Axes.tick_params


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

# 기본적인 형태
# Major tick과 major tick label만 표시된다.
fig, ax = plt.subplots(figsize=(7, 7))
fig.show()
# savefig(fig, __file__, 'tick1.png')

# Axes.tick_params 메서드를 사용하여 tick 설정하기
# major tick의 label의 크기 설정
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20)
fig.show()
# savefig(fig, __file__, 'tick2.png')

# tick의 길이와 두께 변경
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20, length=10, width=3)
fig.show()

# tick과 tick label이 표시되는 위치를 설정할 수 있다.
# bottom에 tick과 tick label을 표시하지 않도록 설정한다.
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20, length=10, width=3,
               bottom=False, labelbottom=False)
fig.show()

# left에 tick과 tick label을 표시하지 않도록 설정한다.
fig, ax = plt.subplots(figsize=(7, 7))
ax.tick_params(labelsize=20, length=10, width=3,
               left=False, labelleft=False)
fig.show()
