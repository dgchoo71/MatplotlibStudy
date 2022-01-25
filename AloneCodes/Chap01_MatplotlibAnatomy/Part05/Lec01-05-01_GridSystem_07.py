# 연습문제 2: tick 위치를 계산하기
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

m_exp, M_exp = 0, 5
n_inter_yticks = 4  # major tick 사이의 간격

n_major_yticks = M_exp - m_exp + 1
n_minor_yticks = (n_major_yticks - 1) * (n_inter_yticks + 1) + 1

major_yticks = np.logspace(m_exp, M_exp, n_major_yticks)
minor_yticks = np.logspace(m_exp, M_exp, n_minor_yticks)

major_xticks = np.logspace(0, 4, 5)

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylim([10 ** m_exp, 10 ** M_exp])

ax.set_xticks(major_xticks)
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)

ax.tick_params(axis='y', which='major', length=10)
ax.tick_params(axis='y', which='minor', length=3)

ax.grid(axis='y', which='major', linewidth=1.5)
ax.grid(axis='y', which='minor', linestyle=':')

fig.show()
plt.close(fig)

