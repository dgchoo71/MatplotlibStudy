# style 적용하기

import matplotlib.pyplot as plt
import numpy as np

# pyplot에 스타일을 적용
plt.style.use('seaborn')

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(7, 7))

axes[0].plot([1, 2, 3])
axes[1].scatter(np.random.normal(0, 1, 10),
                np.random.normal(0, 1, 10))

fig.show()
