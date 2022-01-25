# 축의 범위 지정하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7,7))
ax: Axes = ax

# 축의 범위를 지정하지 않았을 경우
fig.show()

# X, Y 축의 범위를 지정한 경우
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

fig.show()


