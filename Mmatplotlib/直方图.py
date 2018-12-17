

from matplotlib import pyplot as plt
from matplotlib import font_manager


font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\AdobeKaitiStd-Regular.otf", size=10)

x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5","最后的骑士","摔跤吧！爸爸","加勒比海盗5:死无对证","金刚:骷髅岛","极限特工:终极回归","生化危机6:终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3","蜘蛛侠","孙悟空","银河护卫队","情圣","新木乃衣"]

y = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23,5.86]

font = font_manager.FontProperties(fname="C:\Windows\Fonts/ARLRDBD.TTF",size=10)   #路径是本地的字体包

#设置图像大小
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(x)),y)

#设置x轴刻度
# plt.xtick_label = ["{}".format(i) for i in x]

plt.xticks(range(len(x)),x,fontproperties=font,rotation=45)  #第一个参数为文字说明的横坐标个数，第二个参数为文字说明的内容，字体，旋转度数

plt.ylabel("piaofang")
plt.xlabel("movies")

plt.show()