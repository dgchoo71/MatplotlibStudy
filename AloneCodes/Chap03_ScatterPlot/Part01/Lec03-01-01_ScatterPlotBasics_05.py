# Scatter point의 색 사용하기
# 점의 색을 이용하여 3번째 정보를 줄 수 있다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


n_data = 10
x_data = np.linspace(0, 10, n_data)
y_data = np.linspace(0, 10, n_data)

# 색을 나타내기 위한 배열 정의
c_arr = [(c/10, c/10, c/10) for c in range(n_data)]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x_data, y_data, s=500, c=c_arr)

fig.show()
