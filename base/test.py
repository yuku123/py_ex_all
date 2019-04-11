# -- coding: utf-8 --

##python 基础

##使用的field
name = ' AbBb ac Dd ';
name = ' aBbB bc Dh ';
age = 10
bicycles = ['a', 'g', 'c']

##第二章 测试方法
print("变量进行覆盖之后的结果：" + name);
print("字符串首字母转换为大写：" + name.title());
print("字符串转换为大写：" + name.upper())
print("字符串转换为小写：" + name.lower())
print("增加\n\t的表示" + "")

print("去除空格(后删):" + name.rstrip())
print("去除空格(前删):" + name.lstrip())
print("去除空格(全删):" + name.strip())
print("转换类型：" + name + str(age))

##第三章 测试方法(列表元素的api)
print("打印列表:" + str(bicycles))
print("得到列表元素，通过下标获取：" + bicycles[2])
# 修改列表采取替换的方式
bicycles[0] = '1';
print("修改之后的列表为：" + str(bicycles))
# 增加元素的方式
bicycles.append("f")
print("增加元素之后的列表：" + str(bicycles))
# 在列表中插入元素
bicycles.insert(1, "zc")
print("在列表中插入元素：" + str(bicycles))
# 在列表删除元素
del bicycles[1]
print("删除了元素之后：" + str(bicycles))
# 使用pop删除元素，并且使用pop可以放入参数，指定位置弹出
n = bicycles.pop()
print("通过pop返回的元素：" + str(n) + "\t通过pop使用之后的列表：" + str(bicycles))
# 根据值删除元素 remove只能删除第一个值
bicycles.remove("g")
print("根据元素进行删除之后的列表：" + str(bicycles))

# 临时性排序
bicycles.append("h")
bicycles.append("f")
print("临时性排序结果：" + str(sorted(bicycles)))
# 永久性排序
print("接受永久排序前：" + str(bicycles))
bicycles.sort()
print("永久性排序之后的结果：" + str(bicycles))

# 元素反转
bicycles.reverse()
print("元素进行反转之后：" + str(bicycles))
# 列表长度
print("列表长度：" + str(len(bicycles)))

##循环篇
print("----------------------------------循环篇-------------------------------------")
for string in bicycles:
    print(string + ",", end="")

print("\n---------range()----------")
for value in range(1, 5):
    print(str(value) + ",", end="")

print("\n---------list()----------")
value = list(range(1, 10))
print("转换range()，生成数字列表：" + str(value))

print("\n---------对数据列表进行简单的统计计算---------")
print("最小值:" + str(min(value)) + ",最大值：" + str(max(value)) + ",求和：" + str(sum(value)))

print("\n---------列表解析----------")
value = [value ** 2 for value in range(1, 11)]
print("列表解析:" + str(value))

print("\n---------切片：使用列表的一部分（可以直接运用在循环中）----------")
print("输出value列表前三个数据：" + str(value[0:3]))
print("输出value列表前x个数据,：" + str(value[:4]))
print("输出value列表从x开始到末尾：" + str(value[3:]))
print("输出value列表从倒数3个数：" + str(value[-3:]))
value1 = value[:]
value1[1] = 'zc'
print("复制列表(修改复制列表不改变源数据)：" + str(value1))

print("\n---------元组（不可变信息）----------")
value = (1, 2, 4, "zc")
print("这些都是元组信息：" + str(value))

print("\n---------条件测试----------")
if 1 in value:
    print("1在value里面")
elif 1 not in value:
    print("1在value里面")

print("\n---------第六章：字典----------")
value = {'color': 'green', "point": 1}
print("访问字典中point:" + str(value["point"]))
value["add"] = 'add'
print("增加键值对之后的字典" + str(value))
value["add"] = "modified_add"
print("修改了键值对之后的字典：" + str(value))
del value["add"]
print("删除键值对之后：" + str(value))
print("\n--------遍历字典-----------")
for ke,valu in value.items():
    print("key:" + str(ke))
    print("valu:" + str(valu))

for key in value.keys():
    print(value[key])

for value in value.values():
    print(value)

print("\n---------用户输入以及while循环----------")
# 吃掉用户的一个输入，并将这个输入吃掉
#massage = input("yourname")
#print(massage)

print("\n---------函数定义----------")

def f():
    print("这里是f()函数的地方，和一般的java方法一致")

def f_yuan(*a):
    print('这里输出打包好了的元组信息：' + str(a))

f_yuan('a', 'b', 'c')

print("\n---------类----------")

class Dog:
    def __init__(self):
        self.name = "name";
        self.age = "age";

    def sit(self):
        print("i'm sitting")

class Son(Dog):
    def __init__(self):
        super().__init__()
    def a(self):
        print("wo ai a")
son = Son()
son.a()
son.sit()
print("\n-------------------")
print("\n-------------------")
