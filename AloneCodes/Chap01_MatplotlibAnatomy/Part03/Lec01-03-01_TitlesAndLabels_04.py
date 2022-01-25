# 연습 문제

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


figsize = (7, 7)
fig: Figure = plt.figure(figsize=figsize)
ax: Axes = fig.add_subplot()

# 메인 차트의 서식 설정
ax.set_title("Gaussian colored noise", fontsize=20)
ax.set_xlabel("time (s)", fontsize=15)
ax.set_ylabel("Current(nA)", fontsize=15)

# 왼쪽 윈도우 차트
ax_impulse: Axes = fig.add_axes(rect=[0.2, 0.55, 0.25, 0.25])
ax_impulse.set_title("Impulse response", fontsize=15)
ax_impulse.get_xaxis().set_visible(False)
ax_impulse.get_yaxis().set_visible(False)

# 오른쪽 윈도우 차트
ax_prob: Axes = fig.add_axes(rect=[0.6, 0.55, 0.25, 0.25])
ax_prob.set_title("Probability", fontsize=15)
ax_prob.get_xaxis().set_visible(False)
ax_prob.get_yaxis().set_visible(False)

fig.show()
