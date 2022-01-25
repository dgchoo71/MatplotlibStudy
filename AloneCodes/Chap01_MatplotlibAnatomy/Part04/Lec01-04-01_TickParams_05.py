# tick_params 연습
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html?highlight=tick_params#matplotlib.axes.Axes.tick_params


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(10, 10))

ax.tick_params(axis='y',
               labelsize=20, colors='gray')
ax.tick_params(axis='x',
               labelsize=20, rotation=40,
               colors='gray')
ax.set_ylabel("mAP: Unseen Scenes", fontsize=20, color='gray')

fig.show()

