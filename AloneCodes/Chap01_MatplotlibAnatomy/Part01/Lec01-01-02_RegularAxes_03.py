# 정형화된 Axes 생성하기
# unpacking을 이용하여 Axes 객체 사용하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# 2 X 1 Axes 생성하기
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

print(ax1)
print(ax2)
"""
AxesSubplot(0.125,0.53;0.775x0.35)
AxesSubplot(0.125,0.11;0.775x0.35)
"""

plt.show()

# ----
# 1 X 2 Axes 생성하기
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(7, 7), facecolor='linen')

print(ax1)
print(ax2)
"""
AxesSubplot(0.125,0.11;0.352273x0.77)
AxesSubplot(0.547727,0.11;0.352273x0.77)
"""

plt.show()

