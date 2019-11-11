import urllib.request

# 使用代理
def use_proxy(proxy_addr,url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data;
proxy_addr = "114.215.95.188:3128"
data = use_proxy(proxy_addr,"http://www.baidu.com")
print(data)
#c
# file = urllib.request.urlopen("http://www.baidu.com")
# data = file.read()
# dataline = file.readline()
# print(data)
# print(dataline)
#
# # 清理缓存
# urllib.request.urlcleanup()