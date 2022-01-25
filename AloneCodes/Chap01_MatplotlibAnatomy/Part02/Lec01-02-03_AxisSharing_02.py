# 축 공유하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# plt.subplots를 사용하면 가장 간단한 방법으로 축을 공유할 수 있다.
# 단, 가로축을 공유하고 세로축을 따로 공유하는 것은 어렵다.

# 축을 공유하지 않은 상태
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
fig: Figure = fig
fig.show()

# X 축만을 공유한 상태
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7), sharex=True)
fig.show()

# Y 축만을 공유한 상태
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7), sharey=True)
fig.show()

# X, Y 축을 모두 공유한 상태
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7), sharex=True, sharey=True)
fig.show()






