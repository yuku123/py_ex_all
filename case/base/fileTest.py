import json


with open("learn.txt") as a:
    content = a.read()
    print(content.rstrip())

print("------逐行读取------")
with open("learn.txt") as a:
    for line in a:
        print(line.rstrip())

print("------创建各行内容的列表------")
with open("learn.txt") as a:
    lines = a.readlines()
for line in lines:
    print(line.rstrip())

print("---------写文件(a,w,r,r+)---------")

with open("learn.txt",'a') as a:
    a.write("chi\n")

print("-----------异常-----------")
try:
    print("")
    #print(1/0)
except ZeroDivisionError:
    print("aaa")


print("------json相关-------")
number = [1,2,3]
print(number)
with open('learn.txt',"a") as a:
    json.dump(number,a)