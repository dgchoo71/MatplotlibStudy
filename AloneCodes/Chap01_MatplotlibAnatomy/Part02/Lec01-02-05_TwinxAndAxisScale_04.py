# log scale의 밑을 지정할 수 있다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


p = np.linspace(0.001, 0.999, 300)
information = -np.log2(p)

fig: Figure = plt.figure()
ax: Axes = fig.add_subplot()

# log의 밑을 변경한다.
ax.set_yscale('log', base=2)
ax.plot(p, information)

fig.show()





