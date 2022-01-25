# Spine Objects
# https://matplotlib.org/stable/api/spines_api.html
# 축과 spine을 없애고 이미지를 그린다

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np

noise_img = np.random.normal(loc=0, scale=1, size=(100, 100))

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

# 이미지를 그대로 그리면 spine과 tick이 그대로 보인다.
ax.imshow(noise_img)
fig.show()

# spine을 숨긴다.
spine: Spine
for spine in ax.spines.values():
    spine.set_visible(False)
    
# tick, tick label을 숨긴다.
ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)
    
fig.show()
