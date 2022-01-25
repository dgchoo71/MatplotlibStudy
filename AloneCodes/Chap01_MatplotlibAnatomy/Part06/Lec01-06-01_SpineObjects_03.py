# Spine Objects
# https://matplotlib.org/stable/api/spines_api.html
# spine에 접근할 때는 dictionary를 이용한다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine


fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

# spine을 없애도 tick과 ticklabel은 그대로 표시된다.
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

fig.show()

# tick과 tick label을 없애려면 tick_params 메소드를 사용한다.
ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)

fig.show()
plt.close(fig)
