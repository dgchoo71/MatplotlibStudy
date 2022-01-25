# Line 기호를 이용하여 보조선 그리기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 300)
sin = np.sin(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin, color='black')

# max 보조선 그리기
ax.axhline(y=1, linestyle=':', color='red')

# min 보조선 그리기
ax.axhline(y=-1, linestyle=':', color='blue')

fig.show()
