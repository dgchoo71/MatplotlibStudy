import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

# rcParams setting
plt.style.use('seaborn')
plt.rcParams['lines.linewidth'] = 4

# data setting
msr_x = np.linspace(0, 2E5, 10)
msr_y = np.linspace(0, 8E5, 10)

vatex_x = np.linspace(0, 4.1E5, 20)
vatex_en_y = np.linspace(0, 29E5, 20)
vatex_zh_y = np.linspace(0, 28E5, 20)

# plotting
fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(16, 10))

ax.plot(vatex_x, vatex_en_y, color='g',
        label='VATEX-en')
ax.plot(vatex_x, vatex_zh_y, color='b',
        linestyle='--', label='VATEX-zh')
ax.plot(msr_x, msr_y, color='r',
        linestyle='-.', label='MSR-VTT')

# axis customizing
ax.set_ylim([-1E5, 3E6])
y_ticks = np.linspace(0, 25E5, 6)
ax.set_yticks(y_ticks)

# ticks and grid customizing
# 지수표기가 아닌 일반 표기법 사용
ax.ticklabel_format(axis='both', style='plain')
ax.tick_params(labelsize=30)
ax.grid(linewidth=2)

# label customizing
ax.set_xlabel('number of captions', fontsize=30)
ax.set_ylabel('number of types', fontsize=30)

# legend customizing
ax.legend(loc='lower right', fontsize=40)

fig.tight_layout()
fig.show()
