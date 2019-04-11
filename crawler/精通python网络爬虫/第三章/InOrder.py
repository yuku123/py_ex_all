import urllib.request
import urllib.parse
import urllib.error



## 转码
##url = urllib.request.quote("http://www.baidu.com")

url = "http://www.baidu.com"
## 增加post请求体
postdata = urllib.parse.urlencode({"username":"zifang","password":"test"}).encode('utf-8')
req = urllib.request.Request(url,postdata)

## 增加header
req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")

## 请求
try:
    web = urllib.request.urlopen(req,timeout=100)
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)

## 加上这个.decode('utf-8') 可以使出来的东西变漂亮
print(web.read().decode('utf-8'))

##增加代理
def use_proxy(proxy_addr,url):
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8')
    return data
pr = "125.118.150.183:6666"
data = use_proxy(pr,"http://www.baidu.com")
print("----------")
print(data)