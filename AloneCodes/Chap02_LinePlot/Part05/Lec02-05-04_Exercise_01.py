import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


# data setting
data1 = [0.926, 0.974, 0.988, 0.985, 0.979]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_ylim([0.92, 0.99])
# ax.set_xlim([0, 4])

# 붉은 색 squre 점만 표시
ax.plot(data1, 'sr', markersize=10)

# 5개의 xtick 정의
xticks = range(5)
xtick_labels = [
    r'$1^{st}$' + 'Resblocks' + '\n56x56x256xN',
    r'$2^{nd}$' + 'Resblocks' + '\n28x287x5125xN',
    r'$3^{rd}$' + 'Resblocks' + '\n14x14x1024xN',
    r'$4^{th}$' + 'Resblocks' + '\n7x7x2048xN',
    'Global Pool' + '\n1x1x2048xN'
]

# region
#  ytick 정의
major_yticks = np.linspace(0.92, 0.98, 4)

# 표시되는 minor ytick의 개수가 주어진 범위에서 7개이다.
minor_yticks = np.linspace(0.92, 0.98, 7)
# endregion


# tick과 tick labels 보이기
ax.set_xticks(xticks)

# 단, tick label은 왼쪽으로 정렬시킨다.
ax.set_xticklabels(xtick_labels,
                   ha='left')

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)

# tick label 크기
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

# tick의 길이와 방향 설정
# 오른쪽과 왼쪽 스파인에도 tick을 표시한다.
ax.tick_params(which='major',
               length=7, width=1.5, direction='in',
               right=True, top=True)

# 양쪽 y축에 minor tick을 표시
ax.tick_params(which='minor',
               length=5, width=1.5, direction='in',
               right=True)

# 그리드 표시
ax.grid(linestyle=':')

# 축의 레이블 설정
ax.set_ylabel('Rank-1 Accuracy', fontsize=20)

fig.tight_layout()
fig.show()
