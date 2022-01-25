import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


# data setting
name_list = ['PL', 'NL', 'NL-<SeINL', 'NL->SeINL->SeIPL']

x_data = np.linspace(0.5, 1, 30)
y_data = np.empty(shape=(0, len(x_data)))
gamma_list = [6, 7, 8, 12]

for i in range(len(gamma_list)):
    y: np.ndarray = (-0.5) * np.power(x_data, gamma_list[i]) + 1
    y = y.reshape(1, len(x_data))
    
    # y축을 위한 데이터를 아래 방향으로 쌓는다.
    y_data = np.vstack((y_data, y))
    
# plotting
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(12, 12))

for i in range(len(name_list)):
    ax.plot(x_data, y_data[i],
            label=name_list[i],
            marker='o',
            markersize=10)

# spine 설정
# 두께 변경
spine: Spine
for spine_idx, spine in ax.spines.items():
    spine.set_linewidth(3)
    spine.set_alpha(0.5)
    
# axis limit 설정
ax.set_xlim([0.5, 1.0])
ax.set_ylim([0.5, 1.0])

# legend 설정
ax.legend(loc='lower left', fontsize=17)

# tick과 tick label 설정
tick_dict = {'size': 15}
ticks = [round(0.1 * i, 1) for i in range(5, 11)]

ax.set_xticks(ticks)
ax.set_xticklabels(ticks, fontdict=tick_dict)

ax.set_yticks(ticks)
ax.set_yticklabels(ticks, fontdict=tick_dict)

# 축의 label 설정
label_dict = {'size': 20}
ax.set_xlabel('recall', fontdict=label_dict)
ax.set_ylabel('precision', fontdict=label_dict)

# 그리드 설정
ax.grid(linewidth=2, alpha=0.5)

fig.show()

