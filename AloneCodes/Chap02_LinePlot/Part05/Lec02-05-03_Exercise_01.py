import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.spines import Spine
import numpy as np
import numpy.typing as npt


# rcParams setting
plt.rcParams['font.family'] = 'serif'

# data setting
data_dict_list = []
data_dict1 = {'DF': [90, 99, 100, 100, 100],
              'F2F': [77, 98, 99, 100, 100],
              'FS': [91, 96, 98, 99, 100],
              'NT': [94, 95, 97, 98, 100],
              'All': [93, 94, 96, 97, 100]}
data_dict_list.append(data_dict1)
data_dict2 = {'DF': [77, 91, 95, 98, 99],
              'F2F': [60, 91, 95, 98, 99],
              'FS': [81, 91, 95, 98, 99],
              'NT': [77, 85, 90, 92, 95],
              'All': [68, 82, 88, 92, 96]}
data_dict_list.append(data_dict2)
data_dict3 = {'DF': [66, 76, 83, 91, 94],
              'F2F': [55, 67, 72, 88, 91],
              'FS': [60, 75, 80, 88, 91],
              'NT': [66, 71, 72, 80, 82],
              'All': [60, 66, 67, 77, 81]}
data_dict_list.append(data_dict3)

line_name_list = ['Deepfakes', 'Face2Face', 'FaceSwap',
                  'NeuralTextures', 'All']
ylabel_list = ['Accuracy Raw', 'Accuracy HQ', 'Accuracy LQ']

# font dict & color setting
label_dict = {'weight': 'bold',
              'size': 20}
tick_dict = {'weight': 'semibold',
             'size': 15}
color_list = ['royalblue', 'darkorange', 'gray',
              'cornflowerblue', 'gold']

# tick & ticklabel setting
x_ticks = [i for i in range(5)]
y_ticks = [i for i in range(50, 101, 10)]
x_ticklabels = [10, 50, 100, 300, 1000]

# plotting
fig: Figure
axes: npt.NDArray[Axes]
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(13, 13))

ax: Axes
for ax_idx, ax in enumerate(axes.flat):
    # axis limit customizing
    ax.set_ylim([49, 110])
    
    # tick & ticklable customizing
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticklabels)
    
    ax.set_yticks(y_ticks)
    ax.set_ylabel(ylabel_list[ax_idx], fontsize=20)
    
    ax.tick_params(labelsize=20,
                   left=False,
                   bottom=False)
    
    # plotting
    data: dict = data_dict_list[ax_idx]
    for line_idx, (line_k, line_v) in enumerate(data.items()):
        ax.plot(x_ticks, line_v,
                color=color_list[line_idx],
                linewidth=5,
                label=line_name_list[line_idx])
    
    # spine customizing
    spine: Spine
    for spine_lic, spine in ax.spines.items():
        spine.set_visible(False)
        
    # grid customizing
    ax.grid(axis='y')
    ax.grid(axis='x', linewidth=0)
    

# label & legend customizing
ax: Axes = axes[-1]
ax.set_xlabel('Number of videos', fontsize=30)
ax.legend(bbox_to_anchor=(0.5, -0.2),
          loc='upper center',
          fontsize=15,
          ncol=len(line_name_list),
          edgecolor='white')
    
# axes adjust customizing
fig.subplots_adjust(hspace=0.3, bottom=-0.5)

fig.tight_layout()
fig.show()
