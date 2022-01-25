# Scatter Plot과 Line Plot을 동시에 사용하는 예

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


np.random.seed(0)

x_min, x_max = -5, 5
n_data = 300

x_data = np.random.uniform(x_min, x_max, n_data)
y_data = x_data + 0.5 * np.random.normal(0, 1, n_data)

# 선형 회귀선을 위한 데이터
pred_x = np.linspace(x_min, x_max, 300)
pred_y = pred_x

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(x_data, y_data)

# 선형 회귀선 그리기
ax.plot(pred_x, pred_y, color='r', linewidth=3)

fig.show()
