# 군집의 범례와 데이터의 크기를 나타내는 범례 표시하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import matplotlib.cm as cm


np.random.seed(0)

n_class = 5     # 군집의 개수
n_data = 100    # 각 군집당 데이터 개수

# 군집의 색상 정의
cmap = cm.get_cmap('tab20')
colors = [cmap(i) for i in range(n_class)]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))
center_pt = np.random.uniform(-10, 10, (n_class, 2))

for class_idx in range(n_class):
    center = center_pt[class_idx]

    x_data = center[0] + np.random.normal(0, 1, (n_data,))
    y_data = center[1] + np.random.normal(0, 1, (n_data,))
    s_arr = np.random.uniform(10, 40, (n_data,))

    ax.scatter(x_data, y_data,
               s=s_arr ** 2,
               facecolor='None',
               edgecolor=colors[class_idx],
               label=f'class {class_idx}')

ax.legend(loc='upper right',
          fontsize=25)

# =========================
# scatter point의 크기를 표현하는 범례를 차트의 오른쪽에 표시한다.
# 하나의 차트에는 하나의 범례만 사용할 수 있으므로,
# 두번째 범례를 위해 첫번째 차트와 동일한 위치에 축을 생성하여 fake data를 출력한다.

ax2: Axes = ax.twinx()

# 축을 숨긴다.
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

legend_sizes = [10, 20, 30, 40]

for size_idx, legend_size in enumerate(legend_sizes):
    ax2.scatter([], [],
                facecolor='None',
                edgecolor='black',
                linewidth=3,
                s=legend_size ** 2,
                label=str(legend_size))

# fake data의 범례 표시
ax2.legend(loc='center left',
           bbox_to_anchor=(1, 0.5),
           title='Point Size',
           title_fontsize=30,
           fontsize=30,
           labelspacing=1)

fig.tight_layout()
plt.show()
