#!/usr/bin/python
# _*_ encoding=utf-8

from sklearn import datasets
#自己生成数据、线性回归需要
from sklearn.linear_model import LinearRegression
#图像化的工具
import matplotlib.pyplot as plt

#加载数据时候使用load_dataname
#生成数据时候使用makedata
loaded_data = datasets.load_boston()
#sklearn的datasets的获取形式高度统一，上篇的iris数据加载也是此模式
data_X = loaded_data.data
data_Y = loaded_data.target


model = LinearRegression()

#使用线性回归方式对数据进行fit
model.fit(data_X,data_Y)
#模型预测和rel_calssification
print(model.predict(data_X[:4,:]))
print(data_Y[:4])

#创造一些数据点
#samples:创造的集合
#n_features
#noise:决定离散程度
#输出的是每一个属性值*参数值，coef指的是配套参数

print("coef",model.coef_)

#此处指的是和y轴的焦点是哪一个点
print("inter",model.intercept_)

#获取之前训练模型时候的参数
print(model.get_params())
print(model.score(data_X,data_Y))
X,y = datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=10000)

#将数据X，y使用plt绘制出来
# plt.scatter(X,y)
plt.scatter(data_X,data_Y)

#http://blog.csdn.net/ytdxyhz/article/details/51730995关于决定系数的定义：判断回归方程的拟合度，这个是个人查找，下面也会列出此篇博客的概要内容

#将添加的数据以图像形式展现
plt.show()