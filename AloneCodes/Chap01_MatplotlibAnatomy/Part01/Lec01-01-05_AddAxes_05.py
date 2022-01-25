# zoom axes 추가하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure(figsize=(7, 7), facecolor='linen')

ax: Axes = fig.add_subplot(111)
ax_zoom: Axes = fig.add_axes([0.4, 0.4, 0.45, 0.45])

fig.show()
