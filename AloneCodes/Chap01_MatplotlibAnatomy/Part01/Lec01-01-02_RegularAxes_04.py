# 정형화된 Axes 생성하기
# 2 차원 Axes 다루기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np

# 2 X 2 Axes 생성하기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7), facecolor='linen')

print(axes)
# 2차원 ndarray가 생성된다.
"""
[[<AxesSubplot:> <AxesSubplot:>]
 [<AxesSubplot:> <AxesSubplot:>]]
"""

print(axes[0])
"""
[<AxesSubplot:> <AxesSubplot:>]
"""

print(axes[1])
"""
[<AxesSubplot:> <AxesSubplot:>]
"""

fig: Figure = fig
plt.show()

# ------
# 2차원 Axes 를 하나의 리스트로 다루기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7), facecolor='linen')

axes: np.ndarray = axes
for ax_index, ax in enumerate(axes.flat):
    print(ax_index, ax)
    
"""
0 AxesSubplot(0.125,0.53;0.352273x0.35)
1 AxesSubplot(0.547727,0.53;0.352273x0.35)
2 AxesSubplot(0.125,0.11;0.352273x0.35)
3 AxesSubplot(0.547727,0.11;0.352273x0.35)
"""

plt.show()
