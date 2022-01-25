# Spine Objects
# https://matplotlib.org/stable/api/spines_api.html
# 축을 이동하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine


fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

spine: Spine
for spine_loc, spine in ax.spines.items():
    # 왼쪽과 아래쪽의 spine을 감춘다.
    if spine_loc in ['left', 'bottom']:
        spine.set_visible(False)
       
# tick과 tick label을 재설정한다.
ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False,
               top=True, labeltop=True,
               right=True, labelright=True)

fig.show()
plt.close(fig)
