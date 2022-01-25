# 축을 추가하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

# left, bottom, width, height
ax: Axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
fig.show()

