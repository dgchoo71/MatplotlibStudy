# 두 함수 사이의 색칠하기
# 함수의 값이 적은 경우 색영역을 확장하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import numpy.typing as npt

PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 20)
sin = np.sin(t)

fig: Figure
axes: npt.NDArray[Axes]
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))

axes[0].plot(t, sin, color='black')
axes[0].axhline(0, color='black')

# 실제 데이터가 없는 영역을 색이 칠해지지 않는다.
axes[0].fill_between(t, sin,
                color='darkblue',
                alpha=0.3,
                where=sin>=0)

# 데이터가 없는 영역까지 색을 칠하기
axes[1].plot(t, sin, color='black')
axes[1].axhline(0, color='black')

axes[1].fill_between(t, sin,
                color='darkblue',
                alpha=0.3,
                where=sin>=0,
                interpolate=True)

axes[1].fill_between(t, sin,
                color='darkred',
                alpha=0.3,
                where=sin<0,
                interpolate=True)

fig.tight_layout()
fig.show()
