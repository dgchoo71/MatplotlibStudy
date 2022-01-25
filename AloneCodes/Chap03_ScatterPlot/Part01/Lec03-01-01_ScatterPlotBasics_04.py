# Scatter point의 넓이 사용하기
# 점의 넓이를 이용하여 3번째 정보를 줄 수 있다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


n_data = 10
x_data = np.linspace(0, 10, n_data)
y_data = np.linspace(0, 10, n_data)

# 각 점의 넓이를 배열을 이용하여 사용할 수 있다.
# 단, 점들의 배열 크기와 각 점의 넓이의 배열 크기는 동일해야 한다.
# 10의 두배의 넓이는 100이다.
# 500은 10의 약 7배 크기이다.
s_arr = np.linspace(10, 500, n_data)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x_data, y_data, s=s_arr)

fig.show()
