# Line 이름을 이용하여 Line Styles 설정하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


x_data = np.array([0, 1])
y_data = x_data

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

# 기본 solid 라인
ax.plot(x_data, y_data)

# dot 라인
ax.plot(x_data, y_data + 1,
        linestyle='dotted')

# dash 라인
ax.plot(x_data, y_data + 2,
        linestyle='dashed')

# dash와 dot 혼합 라인
ax.plot(x_data, y_data + 3,
        linestyle='dashdot')

fig.show()



