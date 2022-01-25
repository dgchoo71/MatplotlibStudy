# cmap을 이용하여 color array 생성하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap


PI = np.pi
n_point = 100
t = np.linspace(-4 * PI, 4 * PI, n_point)
sin = np.sin(t)

cmap = cm.get_cmap('Reds', lut=n_point)   # cmap은 LinearSegmentedColormap클래스이다.
# print(type(cmap))
# <class 'matplotlib.colors.LinearSegmentedColormap'>

# color array를 미리 만들어서 사용한다.
c_arr = [cmap(c_idx) for c_idx in range(n_point)]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(15, 10))
ax.scatter(t, sin, s=300, c=c_arr)
fig.show()


