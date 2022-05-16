import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

np.random.seed(0)

data = np.random.uniform(low=10, high=100, size=(10,))

# data를 그릴 위치를 임의로 정의할 수 있다.
# index에 맞는 위치에 bar가 그려지게 된다.
data_idx = [0, 2, 4, 5, 7, 9, 10, 11, 12, 13]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.tick_params(labelsize=15)
ax.bar(x=data_idx, height=data)

plt.show()
