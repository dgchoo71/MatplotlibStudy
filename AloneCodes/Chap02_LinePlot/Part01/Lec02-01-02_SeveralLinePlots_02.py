# 하나의 차트에 여러 개의 Line Plot 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np


n_data1, n_data2, n_data3 = 200, 50, 10

x_data1 = np.linspace(0, 200, n_data1)
x_data2 = np.linspace(0, 200, n_data2)
x_data3 = np.linspace(0, 200, n_data3)

random_noise1 = np.random.normal(0, 1, n_data1)
random_noise2 = np.random.normal(1, 1, n_data2)
random_noise3 = np.random.normal(2, 1, n_data3)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

# X 값을 이용
ax.plot(x_data1, random_noise1)
ax.plot(x_data2, random_noise2)
ax.plot(x_data3, random_noise3)

ax.tick_params(labelsize=20)

fig.show()
plt.close(fig)
