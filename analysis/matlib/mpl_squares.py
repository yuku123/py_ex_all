# -- coding: utf-8 --

###############################
#
# 2D的坐标系画图，已经可以解决数学的函数图像问题了
#
###############################

import matplotlib.pyplot as plt

inputvalue = []
squares = []

# 生成一个定制化的数组
for i in range(0, 100):
    inputvalue.append(0.1 * i)
    squares.append((float(i) / 5) ** 2 - 10)
# 向这个函数传入一个数组，然后就会自动进行，1间隔的画图
# 这是最简单的形式
# plt.plot(squares)

# linewidth可以调整线宽
# plt.plot(squares,linewidth=5)

# x轴定制化
plt.plot(inputvalue, squares, linewidth=5)

# 坐标轴添加标签
plt.title("this is title", fontsize=24)
plt.xlabel("x-value", fontsize=20)
plt.ylabel("y-value", fontsize=20)

plt.show()
