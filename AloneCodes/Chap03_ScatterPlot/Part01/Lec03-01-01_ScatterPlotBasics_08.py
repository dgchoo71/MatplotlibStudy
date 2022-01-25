# scatter plot의 점의 넓이와 line plot의 marker size의 관계

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim((-1, 1))

# line plot의 marker 크기는 길이의 개념
ax.plot(-0.5, 0, 'o', markersize=100)

# scatter plot의 size는 넓이의 개념
ax.scatter(0.5, 0, s=100**2)

# ==> 길이의 제곱이 넓이와 같다.

fig.show()
