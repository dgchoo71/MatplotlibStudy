# 점의 색과 넓이를 동시에 사용하기
# 알파값을 이용하여 점의 투명도를 설정해야 시인성을 확보할 수 있다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


np.random.seed(0)

n_data = 500
x_data = np.random.normal(0, 1, n_data)
y_data = np.random.normal(0, 1, n_data)
s_arr = np.random.uniform(100, 500, n_data)

# 0과 1 사이의 값을 이용하여 색상 배열 생성
c_arr = [np.random.uniform(0, 1, 3) for _ in range(n_data)]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

# scatter plot을 그릴 때, 점들의 투명도를 설정할 수 있다.
ax.scatter(x_data, y_data,
           s=s_arr,
           c=c_arr,
           alpha=0.3)

fig.show()
