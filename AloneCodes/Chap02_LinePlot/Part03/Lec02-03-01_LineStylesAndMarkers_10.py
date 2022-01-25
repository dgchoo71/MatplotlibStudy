# fmt 옵션 사용하기
# fmt = '[marker][line][color]'
# fmt 중 marker만 이용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


x_data = np.array([1, 2, 3, 4, 5])

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

# scatter plot과 유사한 결과를 볼 수 있다.
ax.plot(x_data, 'o', markersize=20)
ax.plot(x_data + 1, 'D', markersize=20)
ax.plot(x_data + 2, 'v', markersize=20)

fig.show()
