import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(5, 5))

ax.scatter(0, 0, s=10000)
plt.show()
plt.close(fig)

# ====
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(0, 0, s=10000, facecolor='r')
plt.show()
plt.close(fig)

# =======
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(0, 0, s=10000, facecolor='red', edgecolor='b')
plt.show()
plt.close(fig)

# ===========
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(0, 0, s=10000, facecolor='red', edgecolor='b', linewidth=5)
plt.show()
plt.close(fig)
