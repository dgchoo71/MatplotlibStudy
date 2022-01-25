# 두 함수 사이의 색칠하기
# 함수의 값이 적은 경우 색영역을 확장하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


np.random.seed(6)

n_data = 10
data_idx = np.arange(0, n_data)
noise1 = np.random.normal(0, 1, n_data)
noise2 = np.random.normal(0, 1, n_data)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(data_idx, noise1)
ax.plot(data_idx, noise2)

ax.fill_between(data_idx, y1=noise1, y2=noise2,
                where=noise1>noise2)
fig.show()

# 데이터가 없는 영역까지 색을 칠하기
ax.fill_between(data_idx, y1=noise1, y2=noise2,
                where=noise1>noise2,
                interpolate=True)
fig.show()
