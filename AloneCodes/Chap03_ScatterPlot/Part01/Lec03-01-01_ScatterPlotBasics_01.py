# 기본적인 Scatter plot 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


np.random.seed(0)

n_data = 100
x_data = np.random.normal(loc=0, scale=1, size=n_data)
y_data = np.random.normal(loc=0, scale=1, size=n_data)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

# 차원이 같은 X축 데이터와 Y축 데이터를 사용해야 한다.
ax.scatter(x_data, y_data)
ax.set_xlabel('Scatter Plot')
fig.show()

# Line Plot으로 Scatter Plot처럼 사용하기
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

# marker만 사용하여 Line Plot 그리기
ax.plot(x_data, y_data, 'o')
ax.set_label('Line Plot')
fig.show()
