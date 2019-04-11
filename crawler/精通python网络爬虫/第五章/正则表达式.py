import  re

#pattern = "yum"
pattern = "\wyum"
#pattern = "\Wyum"

string="http://yum.iqanyum.com"
#result1 = re.search(pattern,string)

# 模式修正
result1 = re.search(pattern,string,re.I)

# 三种正则表达式的常见函数
## 从头开始匹配
result1 = re.match(pattern,string)
## 全部匹配
pattern = re.compile(".python.")
result2 = pattern.findall(string)
## 全文本匹配
#result1 = re.search(pattern,string)

## 替换功能
#result1 = re.sub(pattern,"a",string,3)

print(result1)
