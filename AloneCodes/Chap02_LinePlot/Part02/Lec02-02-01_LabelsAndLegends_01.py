# Label과 Legend 추가하기

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

# 아래 명령을 사용해야 legend가 그려진다.
# legend의 위치를 특정하지 않으면 빈 공간에 legend box가 그려지게 된다.
ax.legend()

fig.show()

# -----------
# legend의 글자 크기를 설정할 수 있다.
ax.legend(fontsize=20)
fig.show()
