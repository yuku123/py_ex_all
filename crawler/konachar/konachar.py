import time
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import logging

logging.basicConfig(format='%(levelname)s: %(message)s',level=logging.INFO)

object = open("./konachar.txt", 'w')

def getweb(baseUrl):
    req = urllib.request.Request(baseUrl)
    req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")

    web = urllib.request.urlopen(req)

    html = web.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.select("#post-list-posts")[0].select("li")

    for e in elements:
        alist = e.select("a");
        photo = alist[len(alist)-1]["href"]
        object.writelines(photo+"\n")
        object.flush()
        #print(photo)

def getAll():
    base = "https://konachan.com/post?page=#index&tags=order%3Arandom"
    for i in range(1,12000):
        logging.info("当前正在执行"+str(i)+"页")
        req = base.replace("#index",str(i));
        getweb(req)

#getAll()
getweb("https://konachan.com/post?page=48&tags=order%3Arandom")