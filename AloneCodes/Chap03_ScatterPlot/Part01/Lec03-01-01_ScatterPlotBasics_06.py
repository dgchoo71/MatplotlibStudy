# 점의 색과 넓이를 동시에 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


n_data = 10
x_data = np.linspace(0, 10, n_data)
y_data = np.linspace(0, 10, n_data)

# 넓이를 나타내기 위한 배열 정의
s_arr = np.linspace(10, 500, n_data)

# 색을 나타내기 위한 배열 정의
c_arr = [(c/10, c/10, c/10) for c in range(n_data)]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x_data, y_data,
           s=s_arr,
           c=c_arr)

fig.show()
