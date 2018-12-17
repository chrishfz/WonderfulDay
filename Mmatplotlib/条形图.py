import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 5  #组数
means_men =(20,35,30,35,27)
means_women =(25,32,34,20,25)

fig,ax =plt.subplots()#创捷一个图 和一个对比图
index = np.arange(n_groups)

bar_width = 0.5   #图的宽度
opacoty = 0.4 #透明度

ax.bar(
    index,means_men,bar_width,
    alpha=opacoty,color='b',
)

fig.tight_layout()
plt.show()