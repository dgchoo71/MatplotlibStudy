import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


# data setting
data = [2, 6, 7, 15, 5.5, 8.5, 8, 12, 20, 15, 0.2]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(13, 10))

# 축 설정
ax.set_yscale('log')
ax.set_xlim([0, 12])
ax.set_ylim([0.1, 50])

# tick과 ticklabel 설정
major_yticks = [1, 10]
minor_yticks = [j * 10 ** i for i in range(-1, -1 + 3) for j in range(1, 1 + 9)]
major_xticks = [i for i in range(1, 12)]

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)
ax.set_xticks(major_xticks)

ax.tick_params(labelsize=15, direction='in', length=15)
ax.tick_params(which='minor',
               labelsize=0, direction='in', length=3)

# grid 설정
ax.grid(which='both')

# plotting
ax.plot(major_xticks, data,
        color='black',
        marker='o',
        label='ResNet20 on CIFAR-10',
        linewidth=3,
        markersize=10)

# legend 설정
# legend의 박스 색상과 경계를 흰색으로 설정한다
ax.legend(loc='upper right',
          fontsize=20,
          edgecolor='white',
          facecolor='white')

# label 설정
# label에 latex 문자열을 사용할 수 있다.
ax.set_xlabel('Blocks' + r'$\rightarrow$', fontsize=20)
ax.set_ylabel(r'Toip Hessian Eigenvalue $\rightarrow$', fontsize=20)

fig.show()
