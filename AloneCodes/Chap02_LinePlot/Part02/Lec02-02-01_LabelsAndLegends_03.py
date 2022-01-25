# Legend location

"""
수직 위치 먼저 설정
Location String   Location Code
best = 0
upper right = 1
upper left = 2
lower left = 3
lower right = 4
right = 5
center left = 6
center right = 7
lower center = 8
upper center = 9
center = 10
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np


np.random.seed(0)

n_data = 100
random_noise1 = np.random.normal(loc=0, scale=1, size=n_data)
random_noise2 = np.random.normal(loc=1, scale=1, size=n_data)
random_noise3 = np.random.normal(loc=2, scale=1, size=n_data)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=20)

ax.plot(random_noise1, label='random noise1')
ax.plot(random_noise2, label='random noise2')
ax.plot(random_noise3, label='random noise3')

# legend가 그려지는 위치를 설정한다.
# loc만 지정하면 차트 영역에 legend가 위치하게 된다.
ax.legend(fontsize=20, loc='upper right')
fig.show()

ax.legend(fontsize=20, loc='upper left')
fig.show()

ax.legend(fontsize=20, loc='lower left')
fig.show()

ax.legend(fontsize=20, loc='lower right')
fig.show()
