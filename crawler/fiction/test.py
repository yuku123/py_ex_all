import urllib.request
import urllib.parse
import urllib.error
from bs4 import  BeautifulSoup

category_list = ['http://www.biquge.com.tw/xuanhuan/',
                 'http://www.biquge.com.tw/xiuzhen/',
                 'http://www.biquge.com.tw/dushi/',
                 'http://www.biquge.com.tw/lishi/',
                 'http://www.biquge.com.tw/wangyou/',
                 'http://www.biquge.com.tw/kehuan/',
                 'http://www.biquge.com.tw/kongbu/',
                 'http://www.biquge.com.tw/quanben/'
                 ]

req = urllib.request.Request(category_list[0])
web = urllib.request.urlopen(req)
html = web.read().decode('gbk')

soup = BeautifulSoup(html,'html.parser')
list = soup.select('.r li a')

for i in list :
    print(i['href'])