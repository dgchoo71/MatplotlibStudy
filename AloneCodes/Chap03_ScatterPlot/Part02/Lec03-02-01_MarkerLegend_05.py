# 군집 그래프 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import matplotlib.cm as cm


# 군집 데이터 생성
np.random.seed(0)

n_class = 5  # 5개의 군집을 정의
n_data = 30  # 하나의 군집에 30개의 데이터가 정의된다

center_pt = np.random.uniform(-20, 20, (n_class, 2))
cmap = cm.get_cmap('tab20')
colors = [cmap(i) for i in range(n_class)]

data_dict = {'class' + str(i): None for i in range(n_class)}

for class_idx in range(n_class):
    center = center_pt[class_idx]
    x_data = center[0] + 2 * np.random.normal(0, 1, (1, n_data))
    y_data = center[1] + 2 * np.random.normal(0, 1, (1, n_data))
    data = np.vstack((x_data, y_data))

    data_dict['class' + str(class_idx)] = data

# 그리기
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

for class_idx in range(n_class):
    data = data_dict['class' + str(class_idx)]
    ax.scatter(data[0], data[1],
               s=1000,
               facecolor='None',
               edgecolor=colors[class_idx],
               linewidth=5,
               alpha=0.5,
               label='class' + str(class_idx))

ax.legend(fontsize=20)
plt.show()

