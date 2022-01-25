# fmt 옵션 사용하기
# fmt = '[marker][line][color]'
# fmt 중 marker만 이용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import numpy.typing as npt

PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 200)
sin = np.sin(t)

# marker의 위치
t_mark = t[::5]
sin_mark = np.sin(t_mark)

fig: Figure
esax: npt.NDArray[Axes]
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 20))

axes[0].plot(t, sin, 'bo:')   # color, marker, linestyle

# marker를 줄이는 방법
axes[1].plot(t, sin, 'b:')    # color, linestyle
axes[1].plot(t_mark, sin_mark, 'bo')    # color, marker

fig.show()
