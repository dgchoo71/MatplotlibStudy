# Line Plot을 이용하여 scatter plot처럼 그리기

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

# s 인자는 넓이 개념으로 이해할 수 있다.
ax.scatter(x_data, y_data, s=100)
ax.set_xlabel('Scatter Plot')
fig.show()

# Line Plot으로 그리기
# Line Plot의 markersize 인자는 길이 개념으로 이해할 수 있다.
ax.plot(x_data, y_data, 'o', markersize=10)
ax.set_xlabel('Line Plot')
fig.show()

# 따라서 두 개의 그림의 marker size는 동일하다.
# 그러나 점만 그릴 때는 Scatter Plot이 훨씬 더 빠르다.
