# 여러 개의 차트에 그리기


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np
import numpy.typing as npt

PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 1000)
sin = np.sin(t)
cos = np.cos(t)
tan = np.tan(t)

fig: Figure
axes: npt.NDArray[Axes]
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 10))

axes[0].plot(t, sin)
axes[1].plot(t, cos)
axes[2].plot(t, tan)

fig.tight_layout()
fig.show()

# tangent graph의 Y 축 범위를 설정한 경우
axes[2].set_ylim([-5, 5])
fig.show()
