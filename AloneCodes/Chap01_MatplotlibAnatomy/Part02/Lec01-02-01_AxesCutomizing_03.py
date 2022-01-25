# Axis Layout Adjustment

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig, ax = plt.subplots(figsize=(7, 7))
fig: Figure = fig
ax: Axes = ax
fig.show()

# 축의 값들 제거
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
fig.show()
