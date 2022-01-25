# add_subplot을 이용하여 축을 공유하기
# add_subplot을 이용하여 축을 공유하면, 축의 tick이 모두 표시된다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure = plt.figure(figsize=(7, 7))
ax1: Axes = fig.add_subplot(211)
ax2: Axes = fig.add_subplot(212, sharex=ax1)

ax2.set_xlim([0, 100])
fig.show()