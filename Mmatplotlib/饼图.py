import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font = font_manager.FontProperties(fname=r"C:\Windows\Fonts/AdobeFanHeitiStd-Bold.otf", size=10)

# fig = plt.figure()  创建自定义图像
# ax = fig.add_subplot(111)  subplot可以规划figure划分为n个子图，但每条subplot命令只会创建一个子图
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["360 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries",]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

#图例
ax.legend(wedges, ingredients,
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("食物材料含量",fontproperties=font)

plt.show()