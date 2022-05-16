# Advanced Legend와 Marker 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import matplotlib.cm as cm


np.random.seed(0)

n_class = 10
n_data = 30

# 각 군집의 중심점 생성
center_pt = np.random.uniform(-30, 30, (n_class, 2))

# 각 군집의 색상 생성
cmap = cm.get_cmap('tab20')
colors = [cmap(i) for i in range(n_class)]

data_dict = {f'class{i}': None for i in range(n_class)}

for class_idx in range(n_class):
    center = center_pt[class_idx]

    x_data = center[0] + 3 * np.random.normal(0, 1, (1, n_data))
    y_data = center[1] + 3 * np.random.normal(0, 1, (1, n_data))

    data = np.vstack((x_data, y_data))

    data_dict[f'class{class_idx}'] = data

# 그리기
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))
for class_idx in range(n_class):
    data = data_dict[f'class{class_idx}']
    ax.scatter(data[0], data[1],
               s=1000,
               facecolor='None',
               edgecolor=colors[class_idx],
               linewidth=5,
               alpha=0.5,
               label=f'class{class_idx}')

ax.legend(loc='center left',
          bbox_to_anchor=(1, 0.5),
          fontsize=20,
          ncol=2,
          title='Classes',
          title_fontsize=30,
          edgecolor='None',
          facecolor='None',
          labelspacing=1.5,
          columnspacing=0.5)

fig.tight_layout()
plt.show()
