import numpy as np
import matplotlib.pyplot as plt

x1 = [0, 1,3,7,2,7,5,7]
x2 = [0, 4,2,7,6,4,3,2]
y1 = [0, 1,3,4,6,6,7,9]
y2 = [0, 9,3,5,1,1,2,4]
plt.figure()
line1=plt.plot(x1, y1,"b--",linewidth=1,color="yellow") #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
line2=plt.plot(x2, y2,"--",linewidth=3,color="blue")

# 为第一个线条创建图例
# first_legend = plt.legend(handles = [line1],loc=1)
# second_legend = plt.legend(handles = [line2],loc=1)

#标签
plt.xlabel("time(s)")
plt.ylabel("values(m)")
plt.title("A simpel case")
plt.legend()  #显示图示
plt.show()
plt.savefig("easyplot.jpg")