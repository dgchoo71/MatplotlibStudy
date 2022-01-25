# fmt 옵션 사용하기
# fmt = '[marker][line][color]'

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


x_data = np.array([1, 2, 3, 4, 5])

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(x_data,
        linestyle=':',
        marker='o',
        color='b')

# fmt를 이용하여 그리기
# color를 다양하게 사용할 수 없다. 지정된 color만 사용할 수 있다.
ax.plot(x_data + 1, ':ob')

fig.show()
