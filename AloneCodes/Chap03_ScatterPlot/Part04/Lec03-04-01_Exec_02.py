import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine

import numpy as np

names = ['DFF R-FCN', 'R-FCN', 'FGFA R-FCN']
dff_data = np.array([(0.581, 13.5), (0.598, 12.8),
                     (0.618, 11.7), (0.62, 11.3),
                     (0.624, 10.2), (0.627, 9.8),
                     (0.629, 9.2), (0.63, 9)])
r_data = np.array([(0.565, 11.2), (0.645, 9)])
fgfa_data = np.array([(0.63, 8.8), (0.653, 9.3),
                      (0.664, 9.6), (0.676, 10.1)])

dff_text = ['1:20', '1:15', '1:10', '1:8', '1:5', '1:3', '1:2', '1:1']
r_text = ['Half Model', 'Full Model']
fgfa_text = ['1:1', '3:1', '7:1', '19:1']

# customizing materials setting
colors = ['#5097A0', '#95341F', '#9A5296']
markers = ['o', '^', '*']
markersizes = [400, 380, 500]
data_vars = ['dff', 'r', 'fgfa']

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(18, 15))

for data_idx in range(3):
    # data load
    data_template = f'data = {data_vars[data_idx]}_data'
    text_template = f'text_arr = {data_vars[data_idx]}_text'

    # 문자열을 실행하여 코드 내에 포함시킨다.
    exec(data_template)
    exec(text_template)

    # scatter plotting
    ax.scatter(data[:, 0], data[:, 1],
               s=markersizes[data_idx],
               c=colors[data_idx],
               label=names[data_idx],
               marker=markers[data_idx])

    # 마커 옆에 레이블 출력하기
    for text_idx, text in enumerate(text_arr):
        # 텍스트를 표시할 위치(x, y), 텍스트, 글자 크기
        ax.text(data[text_idx, 0] + 0.002, data[text_idx, 1],
                text, fontsize=25)

# legend 설정
ax.legend(loc='upper right', fontsize=30)

# spine 설정
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right', 'top']:
        spine.set_visible(False)

    if spine_loc in ['left', 'bottom']:
        spine.set_linewidth(3)

# x, y 범위 설정
ax.set_xlim([0.56, 0.685])
ax.set_ylim([8.5, 14])

# x, y 라벨 설정
ax.set_xlabel('mAP', fontsize=50)
ax.set_ylabel('AD', fontsize=50)

# tick & ticklabel 설정
x_ticks = np.arange(0.58, 0.69, 0.02)
y_ticks = np.arange(9, 15, 1)
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.tick_params(labelsize=30, left=False, bottom=False)

# 그리드 표시
ax.grid(linestyle=':', linewidth=2)

plt.show()
