# size array 조정하기

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


def data2size(data: np.ndarray, min_size: np.float_, max_size: np.float_):
    # 주어진 data를 min_size와 max_size의 값들로 변경하기
    copied_data = data.copy()  # 원본 데이터가 변경되면 안 된다.

    # 0으로 offset
    min_value = np.min(copied_data)
    copied_data -= min_value
    
    # normalize
    max_value = np.max(copied_data)
    copied_data /= max_value

    # 주어진 min과 max 사이의 값으로 변경
    interval = max_size - min_size
    copied_data *= interval   # max와 min의 간격을 이용하여 scaling
    copied_data += min_size   # min_size 만큼 데이터를 offset
    
    return copied_data


# scatter plot 그리기
n_data = 10
x_data = np.linspace(0, 10, n_data)
y_data = np.linspace(0, 10, n_data)
z_data = np.random.normal(0, 1, n_data)  # scatter의 크기

# z_data의 배율 적용
s_arr = data2size(z_data, 100, 2000)

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x_data, y_data, s=s_arr)

plt.show()




