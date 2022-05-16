import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


n_data = 100
x_data: np.ndarray = np.random.normal(0, 1, (n_data,))
y_data: np.ndarray = np.random.normal(0, 1, (n_data,))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(5, 5))

# 마커의 안쪽을 투명으로 설정하여 겹치는 마커를 확실히 구분할 수 있게 한다.
ax.scatter(x_data, y_data, s=300,
           facecolor='None',
           edgecolor='tab:blue',
           linewidth=5)
plt.show()
plt.close(fig)
