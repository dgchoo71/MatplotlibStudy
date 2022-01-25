# 0~255 사이의 색상값을 이용하기
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np


# 0~255 사이의 값을 받아들여 0~1 사이의 값을 되돌리는 함수
convert255to1 = lambda *RGB255: [c / 255 for c in RGB255]

# PPT의 바탕색과 동일한 색상을 사용한다.
ppt_color = convert255to1(128, 85, 128)

label_font_dict = dict(color='w', fontsize=20)  # 흰색

# Figure와 차트 영역의 배경색을 변경한다
fig: Figure = plt.figure(figsize=(20, 10), facecolor=ppt_color)
ax: Axes = fig.add_subplot(facecolor=ppt_color)

ax.plot(np.random.normal(0, 1, (100,)), color='w')
ax.set_xlabel("Data Index", fontdict=label_font_dict)
ax.set_ylabel("Random Value", fontdict=label_font_dict)
ax.tick_params(colors='w', labelsize=20)

spine: Spine
for spine_loc, spine in ax.spines.items():
    spine.set_color('w')
    
fig.subplots_adjust(bottom=0.1, top=0.9,
                    left=0.1, right=0.9)

fig.show()
