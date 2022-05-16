import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

np.random.seed(0)

n_data = 10
data = np.random.uniform(low=10, high=100, size=(n_data,))

# data를 그릴 위치
data_idx = np.arange(n_data)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.tick_params(labelsize=15)
ax.bar(x=data_idx, height=data)

plt.show()
