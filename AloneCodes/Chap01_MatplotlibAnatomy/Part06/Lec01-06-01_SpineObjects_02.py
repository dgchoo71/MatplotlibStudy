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

# 윗쪽과 오른쪽의 spine을 숨긴다
spine: Spine
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right', 'top']:
        spine.set_visible(False)
        
fig.show()
