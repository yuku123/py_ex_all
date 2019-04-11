from pandas import Series,DataFrame
import  pandas as pd
import  numpy as np

##简单series
Obj = Series([1,3,5,6])
print("Series整体打印："+str(Obj))
print("Series值对打印："+str(Obj.values))
print("Series键对打印："+str(Obj.index))
##自定义键
Obj = Series([1,3,5,6],index=['d','a','c','u'])
print("Series整体打印："+str(Obj))
print("Series值对打印："+str(Obj.values))
print("Series键对打印："+str(Obj.index))
##取值
print("取值："+str(Obj['a']))
print("取值："+str(Obj[['a','d']]))
##运算
print("运算取值：\n"+str(Obj[Obj>3]))
print("运算取值：\n"+str(Obj*2))
##从字典创造series
sdata={'a':1,'b':3,'d':5,'u':9}
Obj=Series(sdata)
print("从字典创造：\n"+str(Obj))
##通过一个字典和key数组实现排序
Obj=Series(sdata,index=['b','d','u'])
print("通过一个字典和key数组实现排序:\n"+str(Obj))
##监测是否为null
obj_isnull=pd.isnull(Obj)
print("是否为null:\n"+str(obj_isnull))
##数据对齐




