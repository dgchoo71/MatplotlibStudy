# Named Colors (Base Colors)

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# 색상의 이름을 이용하기
color_list = 'bgrcmy'

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, len(color_list)])

for c_idx, c in enumerate(color_list):
    ax.text(0, c_idx, f'color={c}', fontsize=20,
            ha='center', color=c)
    
fig.show()
