# coding=utf-8

import threading
import urllib.request
import urllib.parse
import urllib.error
import os
from bs4 import BeautifulSoup


class threadbean(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.localpath='/Users/zifang/Downloads/books'
        self.url_base='http://www.biquge.com.tw'

    def run(self):
        try:

            req = urllib.request.Request(self.url)
            req.add_header("User-Agent",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
            web = urllib.request.urlopen(req)
            html = web.read().decode('gbk')
            #print(html)

            soup = BeautifulSoup(html, 'html.parser')

            bookname = soup.select('#info h1')[0].get_text()
            charpter = soup.select('dd a')

            if not os.path.exists(self.localpath) :
                os.makedirs(self.localpath)
            file = open(self.localpath+"/"+bookname+'.txt','w',encoding='utf-8')

            # 100章：url
            dicts = {}

            for i in charpter:
                sub_net = i['href']
                sub_name = i.get_text()
                dicts[sub_name] = self.url_base + sub_net

            # 遍历字典，得到整本书的数据
            for key, value in dicts.items():
                content = str(crawler_from_page(value))
                header = str(key + ":" + value)
                file.write(header)
                file.write(content)
                file.flush()

                #print(crawler_from_page(value))
                #print(key + ":" + value)
        except BaseException:
            print("error:"+self.url)


def crawler_from_page(url_part):
    html = urllib.request.urlopen(url_part).read().decode('gbk')
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select('#content')[0].get_text()
    return content