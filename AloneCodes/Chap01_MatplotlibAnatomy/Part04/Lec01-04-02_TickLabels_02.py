# 축의 레이블을 변경한다.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html

# Axes.set_xticks를 설정하고 난 뒤, Axes.set_xticklabels를 설정해야 한다.

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

xticks = [i for i in range(7)]
xtick_labels = [
    " ",
    "<vehicle, move along, street>",
    "<person, move along, sidewalk>",
    "<pet, move along, sidewalk>",
    "<person, stay, lawn>",
    "<person, move away (home), driveway>",
    " "]

yticks = [i / 10 for i in range(11)]

fig: Figure
ax: Axes

fig, ax = plt.subplots(figsize=(20, 10))

ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels, ha='right')  # rotation의 중심을 right로 변경

ax.set_yticks(yticks)

ax.tick_params(axis='x', rotation=20, labelsize=15, colors='gray')
ax.tick_params(axis='y', labelsize=15, colors='gray')

fig.subplots_adjust(bottom=0.2, top=0.95,
                    left=0.1, right=0.9)

fig.show()
