# -- coding: utf-8 --

###############################
#
# 散点图
#
###############################

import matplotlib.pyplot as plt

#散点图,点和点的大小
# plt.scatter(2,4,s=90)

# 绘画数组形式的散点图
x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]
plt.scatter(x_value,y_value)
#删除数据点的轮廓线
#plt.scatter(x_value,y_value,edgecolor='none',s=40)

#增加点的颜色
#plt.scatter(x_value,y_value,c='red',edgecolor='none',s=40)


#各种设置
plt.title("this is title",fontsize=24)
plt.xlabel("x-value",fontsize = 20)
plt.ylabel("y-value",fontsize=20)

#设置图的显示区间
plt.axis([0,10,0,10])

#显示
plt.show()