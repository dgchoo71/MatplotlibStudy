# 두 함수 사이의 색칠하기
# 해칭 패턴 : {'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

PI = np.pi
t = np.linspace(-4 * PI, 4 * PI, 200)
sin = np.sin(t)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(t, sin, color='black')
ax.axhline(0, color='red')

# 투명도 설정
ax.fill_between(t, sin, alpha=0.3)
fig.show()

# 해칭 설정
ax.fill_between(t, sin, facecolor='white',
                hatch='/', edgecolor='b')
fig.show()

# 해칭 밀도 설정
# edgecolor 인자를 이용하여 해칭선의 색을 설정
ax.fill_between(t, sin, facecolor='white',
                hatch='///', edgecolor='b')
fig.show()
