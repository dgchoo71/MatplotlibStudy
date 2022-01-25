# 하나의 차트에 여러 개의 Line Plot 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np


n_data = 100

random_noise1 = np.random.normal(0, 1, n_data)
random_noise2 = np.random.normal(1, 1, n_data)
random_noise3 = np.random.normal(2, 1, n_data)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(random_noise1)
ax.plot(random_noise2)
ax.plot(random_noise3)

ax.tick_params(labelsize=20)

fig.show()
