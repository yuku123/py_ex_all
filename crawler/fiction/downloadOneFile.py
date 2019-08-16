import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup


def crawler_from_page(url_part):
    html = urllib.request.urlopen(url_part).read().decode('gbk')
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select('#content')[0].get_text()
    return content


# 基于此网页进行爬虫
url_base = 'http://www.biquge.com.tw'
url = 'http://www.biquge.com.tw/0_469/'

req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")

web = urllib.request.urlopen(req)
html = web.read().decode('gbk')

soup = BeautifulSoup(html, 'html.parser')

bookname = soup.select('#info h1')[0].get_text()
charpter = soup.select('dd a')

# 100章：url
dicts = {}

for i in charpter:
    sub_net = i['href']
    sub_name = i.get_text()
    dicts[sub_name]=url_base+sub_net


# 遍历字典，得到整本书的数据
for key,value in dicts.items():
    print(crawler_from_page(value))
    print(key+":"+value)