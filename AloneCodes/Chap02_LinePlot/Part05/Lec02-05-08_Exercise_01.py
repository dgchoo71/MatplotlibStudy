# fill_between 사용 예제

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


# 데이터 준비
data_loc = [46, 58, 65, 73, 80, 92, 96, 98]
supervised_data = [60, 65, 63, 80, 68, 70, 78, 85]
supervised_top_data = [98, 110, 90, 150, 125, 120, 130, 140]
supervised_bottom_data = [40, 30, 45, 30, 40, 40, 40, 40]
distilled_data = [25, 26, 15, 30, 24, 44, 49, 51]
distilled_top_data = [48, 55, 41, 48, 44, 55, 52, 86]
distilled_bottom_data = [5, 0, 7.5, 15, 10, 0, 20, 17]

# plotting
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(13, 10))

# 두 데이터 라인 사이을 채우기
ax.fill_between(data_loc,
                y1=supervised_top_data,
                y2=supervised_bottom_data,
                color='dodgerblue',
                alpha=0.4)

ax.fill_between(data_loc,
                y1=distilled_top_data,
                y2=distilled_bottom_data,
                color='peachpuff',
                alpha=1)

# 라인 그래프 그리기
ax.plot(data_loc, supervised_data,
        marker='x',
        color='dodgerblue',
        linewidth=3,
        markersize=15,
        label='Supervised Student')

ax.plot(data_loc, distilled_data,
        marker='o',
        markersize=15,
        markerfacecolor='peachpuff',
        markeredgewidth=3,
        color='darkorange',
        label='Distilled Student')

ax.axhline(y=25,
           color='black',
           linestyle='--',
           linewidth=3,
           label='Supervised Teacher')

# 축 설정
ax.set_xlim([45, 100])
ax.set_ylim([0, 200])

# spine 설정
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right', 'top']:
        spine.set_visible(False)
    
    if spine_loc in ['left', 'bottom']:
        spine.set_linewidth(1.8)
        
# tick과 tick label 설정
x_ticks = np.arange(50, 91, 10)
y_ticks = np.arange(0, 201, 50)

ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)

ax.tick_params(direction='in',
               length=5,
               width=1.8,
               labelsize=25)

# legend 설정
ax.legend(loc='upper left',
          fontsize=20)

# 축의 label 설정
label_font_dict = {'size': 30}
ax.set_xlabel('Distillation Rate (%)', fontdict=label_font_dict)
ax.set_ylabel('RMS Absolute Pose Errors (m)', fontdict=label_font_dict)

fig.show()