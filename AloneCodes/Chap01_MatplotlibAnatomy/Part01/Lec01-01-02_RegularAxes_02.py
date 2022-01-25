# 정형화된 Axes 생성하기
# plt.subplots() 메서드 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np

# 3 X 1 Axes 생성하기
fig: Figure
axes: np.ndarray
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 7), facecolor='linen')

print(type(axes))
print(axes[0])
print(axes[1])
print(axes[2])
"""
AxesSubplot(0.125,0.653529;0.775x0.226471)
AxesSubplot(0.125,0.381765;0.775x0.226471)
AxesSubplot(0.125,0.11;0.775x0.226471)
"""

fig: Figure = fig
plt.show()

# ----
# 1 X 3 Axes 생성하기
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(7, 7), facecolor='linen')

print(axes[0])
print(axes[1])
print(axes[2])
"""
AxesSubplot(0.125,0.11;0.227941x0.77)
AxesSubplot(0.398529,0.11;0.227941x0.77)
AxesSubplot(0.672059,0.11;0.227941x0.77)
"""

plt.show()
