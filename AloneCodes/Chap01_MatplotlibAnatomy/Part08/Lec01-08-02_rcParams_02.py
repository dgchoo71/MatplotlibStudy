# rcParams를 이용하여 기본적인 스타일들을 설정할 수 있다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# pyplot에서 적용할 수 있는 값들을 미리 지정해 놓는다.
# 기본적으로 설정을 해 놓으면 편리하다.
plt.rcParams['figure.figsize'] = [6.4, 4.8]
plt.rcParams['axes.titlesize'] = 30
plt.rcParams['axes.labelcolor'] = 'darkblue'
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['grid.linestyle'] = ':'


fig: Figure
ax: Axes

# 속성을 일일이 지정할 필요없이 rcParam에서 적용한 값을 사용하게 된다.
fig, ax = plt.subplots()

ax.set_title('Title')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.grid()

fig.show()
plt.close(fig)
