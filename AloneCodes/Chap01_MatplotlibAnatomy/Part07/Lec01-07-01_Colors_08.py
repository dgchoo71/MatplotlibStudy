# Auto Colormap

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
import matplotlib.cm as cm

import numpy as np

harvest = np.array([[0.9, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                   [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                   [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                   [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                   [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                   [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                   [0.1, 2.0, 2.0, 1.4, 0.0, 1.9, 6.3]])

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

# matplotlib의 기본 colormap인 viridis를 사용한다.
im: AxesImage = ax.imshow(harvest)

fig.show()
