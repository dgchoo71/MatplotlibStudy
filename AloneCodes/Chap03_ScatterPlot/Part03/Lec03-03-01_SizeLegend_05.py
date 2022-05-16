# Scatter point의 크기를 범례로 같이 출력하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

n_data = 100
x_data = np.random.normal(0, 3, (n_data,))
y_data = np.random.normal(0, 3, (n_data,))
s_arr = np.random.uniform(10, 50, (n_data,))  # scatter 크기

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))

# 데이터를 차트에 표시하기
ax.scatter(x_data, y_data,
           s=s_arr ** 2,
           facecolor='None',
           edgecolor='blue',
           linewidth=4)

# ==========
# 데이터의 크기를 범례로 표시하기
legend_sizes = np.array([10, 20, 30, 40, 50])

# 범례를 그리기 위한 fake data plot
for legend_size in legend_sizes:
    ax.scatter([], [],
               facecolor='None',
               edgecolor='blue',
               linewidth=3,
               s=legend_size ** 2,
               label=f'{legend_size}')

# 범례 표시
ax.legend(loc='center left',
          bbox_to_anchor=(1, 0.5),
          title='Point Size',
          title_fontsize=30,
          fontsize=30,
          labelspacing=1)

fig.tight_layout()
plt.show()
