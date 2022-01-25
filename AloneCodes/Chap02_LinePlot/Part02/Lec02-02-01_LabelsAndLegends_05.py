# Legend의 기준 위치 설정하기 (bbox_to_anchor와 loc 매개 변수를 동시에 사용한다)
# bbox_to_anchor와 loc를 사용하면, loc는 차트에서의 legend box의 위치를 의미하지 않는다.
# bbox_to_anchor로 지정한 위치에 legend box가 붙을 위치를 의미한다.

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

# bbox_to_anchor를 기준 점으로 legend box의 center left가 위치한다.
ax.legend(fontsize=20,
          bbox_to_anchor=(1, 0.5),
          loc='center left')
fig.tight_layout()
fig.show()

# -------------
ax.legend(fontsize=20,
          bbox_to_anchor=(1, 0.5),
          loc='center right')
fig.tight_layout()
fig.show()

# -------------
ax.legend(fontsize=20,
          bbox_to_anchor=(-0.1, 0.5),
          loc='center right')
fig.tight_layout()
fig.show()

# -------------
ax.legend(fontsize=20,
          bbox_to_anchor=(0.5, 1),
          loc='lower center')
fig.tight_layout()
fig.show()

# -------------
ax.legend(fontsize=20,
          bbox_to_anchor=(0.5, -0.1),
          loc='upper center')
fig.tight_layout()
fig.show()
