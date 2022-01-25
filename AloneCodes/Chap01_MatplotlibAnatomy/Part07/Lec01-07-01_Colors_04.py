# RGB 색상 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


color_list: list = [(1., 0., 0.),
                    (0., 1., 0.),
                    (0., 0., 1.)]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, len(color_list)])

for c_idx, c in enumerate(color_list):
    c_string_list = [c for c in str(c)]
    c_string = ''.join(c_string_list)
    
    ax.text(0, c_idx, f'color = {c_string}',
            fontsize=20, ha='center', color=c)
    
fig.show()
