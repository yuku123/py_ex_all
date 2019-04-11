# -- utf-8--
import numpy as np
import matplotlib.pyplot as plt

##创造
print('-----------------基本操作-------------------')
data=[
    [2,5,7],
    [2,5,8],
    [2,5,8],
    [2,5,8]]
## 多维数组对象
arr = np.array(data)
print("打印这个多维数组的内容：\n"+str(arr))
print("打印这个多维数组的形状"+str(arr.shape))
print("打印这个多维数组的维度(嵌套几层)"+str(arr.ndim))

print("创建zero(4,2,3)\n"+str(np.zeros((4,2,3))))
print("创建empty(2,3)\n"+str(np.empty((2,3))))
print("range(2,10)\n"+str(np.arange(2,10)))
print("得到data的dtype:"+str(arr.dtype))

print('-----------------切片操作-------------------')

data=np.arange(10)
print("data的值为:"+str(data))
print("data索引："+str(data[5]))
print("data切片："+str(data[2:8]))

data[2:8]=1
print("对data进行广播赋值："+str(data))
print("必须显式赋值："+str(data.copy()))

data=np.zeros((5,5,5))
data[:,1:4,1:4]=1
print(str(data))

print("------------------随机数------------------")
# data=np.random.randn(100,100)
# print(str(data))
#
# np.random.normal(size=100)
# np.random.normal(size=(10, 10))
#
# year=list(np.arange(-3,3,0.01))
# pop=np.random.randn(10000)
# print(str(pop))
# re=[]
# for y in year:
#     i=0
#     for p in pop:
#         if -1<=p-y<=1:
#             i=i+1
#     re.append(i)
# print(len(year))
# print(len(re))
# # 1.线图
# #调用plt。plot来画图,横轴纵轴两个参数即可
# plt.plot(year,re)
# # python要用show展现出来图
# plt.show()

print("--------通过布尔值进行切片---------")

names = np.array(['a','b','c','a','d','e'])
data = np.random.randn(6,3)

print("name:\n"+str(names))
print("data:\n"+str(data))
print("names==a:"+str(names=='a'))
data=data[(names=='a')|(names=='b'),:2]#可以多条件
print(str(data)+"\n")

data[data<0]=0
print(str(data))

print("------------花式索引---难，不能理解-----------")
##按顺序进行选取子集
data = np.random.randn(6,3)
print("data:\n"+str(data))
data = data[[1,2,0,4]]
print("data选择之后：\n"+str(data))

print("----------转置---------")
data=np.arange(15).reshape(3,5)
print(data)
print(data.T)
print("--------数据处理-----------")
points=np.arange(-5,5,0.01)
xs,ys=np.meshgrid(points,points)
z=np.sqrt(xs**2+ys**2)
print(str(z))
plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()


