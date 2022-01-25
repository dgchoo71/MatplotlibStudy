# Horizontal Line 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

ax.axhline(y=1, color='black', linewidth=1)

# 수평선의 범위를 지정할 수도 있다.
# 이 때, 범위값은 0 ~ 1 사이의 값을 사용한다.
ax.axhline(y=2, color='black', linewidth=1,
           xmax=0.8, xmin=0.2)

fig.show()
