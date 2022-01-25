# 정형화된 Axes 생성하기
# plt.subplots() 메서드 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


fig: Figure = plt.figure()

ax1: Axes = fig.add_subplot(211)
ax2: Axes = fig.add_subplot(212)

# Axes의 좌표와 크기를 출력한다.
print(ax1)
print(ax2)
"""
AxesSubplot(0.125,0.53;0.775x0.35)
AxesSubplot(0.125,0.11;0.775x0.35)
"""

# ------
# plt.subplots() 메서드를 이용하여 정형화된 Axes들을 생성할 수 있다.
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(7, 7), facecolor='linen')
print(axes)
"""
[<AxesSubplot:> <AxesSubplot:>]
"""

# 여러 개의 axes가 ndarray 형식으로 생성된다.
print(type(axes))
"""
<class 'numpy.ndarray'>
"""

print(axes[0])
print(axes[1])
"""
AxesSubplot(0.125,0.53;0.775x0.35)
AxesSubplot(0.125,0.11;0.775x0.35)
"""

