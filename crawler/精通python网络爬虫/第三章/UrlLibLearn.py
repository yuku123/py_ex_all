import urllib.request

#file = open("web.html",'w')
## 请求得到一个网页（想象为一个文件）
web = urllib.request.urlopen("http://www.baidu.com")      ## print() -> <http.client.HTTPResponse object at 0x10b915588>
web.info()
web.getcode()
web.geturl()
## 获得这个文本的全部信息赋值为一个字符串
data_string_of_file = web.read()
## 获得这个文本的全部信息赋值为一个字符串
data_list_of_file = web.readlines() ## 上面这种方式取完之后，则file内为空,可以遍历出值
## 写入文件
#file.write(web)

print(data_string_of_file)
## 清空缓存
urllib.request.urlcleanup()
