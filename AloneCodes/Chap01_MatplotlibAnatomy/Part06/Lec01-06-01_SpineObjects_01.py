# Spine Objects
# https://matplotlib.org/stable/api/spines_api.html
# spine에 접근할 때는 dictionary를 이용한다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine


fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(7, 7))

print(type(ax.spines))
print(ax.spines)

print(list(ax.spines.keys()))
print(list(ax.spines.values()))
