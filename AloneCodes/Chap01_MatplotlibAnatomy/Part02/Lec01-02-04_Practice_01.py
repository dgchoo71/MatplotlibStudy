# 기본적인 형식으로 여러 축들을 그리기

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy.typing as npt


fig: Figure = plt.figure(figsize=(20, 10))

n_row, n_col = 3, 4
axes: npt.NDArray[Axes] = np.empty(shape=(0,))

xlabel_list: list = ['Iteration 01', 'Iteration 11', 'Iteration 21', 'Iteration 31']
ylabel_list: list = ['Log-Likelihood', 'Negative Grad.', 'Probability']
ylim_list: list = [[1.5, 2.0], [-0.7, 0.7], [0, 0.14]]
xlim_list: list = [[0, 100], [0, 200], [0, 300], [0, 400]]

for r_idx in range(n_row):
    
    for c_idx in range(n_col):
        ax = fig.add_subplot(n_row, n_col,
                             n_col * r_idx + c_idx + 1)
        
        ax: Axes = ax

        # Y 축 공유 설정하기 (첫번째 열이 아니면 바로 이전의 축을 공유)
        if c_idx > 0:
            ax.sharey(axes[-1])
            
        # X 축 공유 설정하기 (첫 행에서 만들어진 축을 공유)
        if r_idx > 0:  # 0, 1, 2, 3만 출력이 되어야 한다.
            ax.sharex(axes[c_idx])

        # 데이터 그리기
        ax.plot([], marker='|', color='b', label='regression')
        ax.plot([], marker='o', color='r', label='cross entropy')
        ax.plot([], marker='v', color='g', label='target')
        ax.legend()
        
        axes = np.append(axes, ax)

# 축의 레이블 설정하기
for ax_idx, ax in enumerate(axes):
    ax: Axes = ax

    # 첫번째 열에 Y축의 레이블 설정
    if ax_idx % n_col == 0:
        ax.set_ylabel(ylabel_list[ax_idx // n_col], fontsize=20)
        
    # 마지막 행에 X축의 레이블 설정
    if ax_idx >= 2 * n_col:
        ax.set_xlabel(xlabel_list[ax_idx - 2 * n_col], fontsize=20)
        
# 축의 범위 설정
for r_idx in range(n_row):
    axes[r_idx * n_col].set_ylim(ylim_list[r_idx])

for c_idx in range(len(axes) - 4, len(axes)):
    axes[c_idx].set_xlim(xlim_list[c_idx - (len(axes) - 4)])
    
    
fig.tight_layout()
fig.show()

