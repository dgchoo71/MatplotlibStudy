import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib.cm as cm
import numpy as np


# data & utility setting
def data2size(data: list, min_size, max_size) -> list:
    data_copy = data.copy()

    min_val = np.min(data_copy)
    data_copy -= min_val    # 기준점이 0이 되도록 offset

    max_val = np.max(data_copy)
    data_copy /= max_val    # 0~1 사이의 값으로 변환

    interval = max_size - min_size
    data_copy *= interval   # 0 ~ interval 사이의 값으로 변환
    data_copy += min_size   # min_size ~ max_size 사이의 값으로 offset

    return data_copy


countries = ['Australia', 'Austria', 'Belgium', 'Canada', 'Chile',
             'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
             'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland',
             'Israel', 'Italy', 'Japan', 'Korea', 'Luxembourg',
             'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland',
             'Portugal', 'Slovak Republic', 'Slovenia', 'Spain', 'Sweden',
             'Switzerland', 'Turkey', 'United Kingdom', 'United States']

population_densitiy = [3, 101, 367, 4, 23,
                       133, 130, 29, 16, 117,
                       227, 86, 106, 3, 65,
                       365, 203, 337, 501, 207,
                       60, 406, 17, 13, 122,
                       116, 110, 103, 91, 21,
                       194, 97, 257, 32]

private_expenditure = [1.3, 8.9, 10.0, 10.9, 12.8,
                       13.0, 13.2, 13.4, 13.5, 14.8,
                       15.0, 15.8, 16.7, 17.1, 17.2,
                       17.4, 18.1, 18.1, 18.7, 18.9,
                       19.0, 19.0, 19.5, 19.9, 20.0,
                       21.5, 21.6, 23.0, 24.0, 25.0,
                       25.9, 26.7, 28.0, 34.3]

gdp = [38.7, 37.4, 33.6, 37.5, 16.4,
       24.5, 33.2, 19.3, 32.1, 32.0,
       36.2, 19.8, 17.8, 37.7, 37.7,
       29.4, 26.6, 32.0, 31.0, 67.9,
       13.4, 38.4, 27.0, 48.2, 18.9,
       20.9, 21.8, 24.2, 26.8, 36.2,
       42.5, 13.9, 35.6, 45.7]

gdp_size = data2size(gdp, 30, 80)

# color array setting
cmap = cm.get_cmap('tab20', lut=int(len(countries) / 2))
c_arr = [cmap(i) for i in range(int(len(countries) / 2))]

fig: Figure
ax: Axes
fig, ax = plt.subplots(figsize=(20, 10))


# group1 scatter setting
ax.scatter(population_densitiy[:17],
           private_expenditure[:17],
           s=gdp_size[:17] ** 2,
           c=c_arr,
           alpha=0.5,
           hatch='/')

# group2 scatter setting
ax.scatter(population_densitiy[17:],
           private_expenditure[17:],
           s=gdp_size[17:] ** 2,
           c=c_arr,
           alpha=0.5,
           hatch='.')

#  x and y limit customizing
ax.set_xlim([-50, 550])
ax.set_ylim([-3, 40])

# x and y label customizing
ax.set_xlabel("Population Density(Inh./km2",
              fontsize=30)
ax.set_ylabel("Private Expenditure",
              fontsize=30)

# # ticklabel and grid customizing
ax.tick_params(labelsize=20)
ax.grid()

# # country legend customizing
# marker에 하나씩 색상을 지정할 때는 scatter 함수의 옵션으로
# color 대신 faceclor 매개변수를 이용하여 색상을 지정해야
# 해칭을 볼 수 있다.
for country_idx in range(17):
    ax.scatter([], [],
               # color=c_arr[country_idx],
               facecolor=c_arr[country_idx],
               s=500,
               label=countries[country_idx],
               hatch='/')

for country_idx in range(17):
    ax.scatter([], [],
               # color=c_arr[country_idx],
               facecolor=c_arr[country_idx],
               s=500,
               label=countries[country_idx + 17],
               alpha=0.5,
               hatch='.')

ax.legend(bbox_to_anchor=(1, 1),
          loc="upper left",
          ncol=2,
          labelspacing=2)

# size legend customizing
legend_gdp = [float(i) for i in range(10, 61, 15)]
legend_sizes = data2size(legend_gdp, 30, 80)

ax2: Axes = ax.twinx()
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

for legend_idx, legend_size in enumerate(legend_sizes):
    ax2.scatter([], [],
                color='tab:blue',
                s=legend_size ** 2,
                label=legend_gdp[legend_idx])

ax2.legend(loc='lower center',
           bbox_to_anchor=(0.5, 1.05),
           title='GDP Value',
           title_fontsize=30,
           ncol=len(legend_gdp),
           labelspacing=2,
           edgecolor='None',
           handletextpad=2,   # 마커와 텍스트 사이의 간격을 조정한다.
           fontsize=20)

# 오른쪽의 legend를 표시하기 위해 fig 영역의 크기를 조절한다.
fig.subplots_adjust(right=0.75, left=0.05, top=0.75)
plt.show()
