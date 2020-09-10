import time
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup


def getweb(baseUrl):
    req = urllib.request.Request(baseUrl)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")

    web = urllib.request.urlopen(req)

    html = web.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getList(baseUrl):
    soup = getweb(baseUrl)
    element = soup.select(".box.boxshadow")
    map = {}
    for e in element:
        name = e.select("a")[0].text
        href = e.select("a")[0]["href"]
        map[name]=href

    for k,v in map.items():
        print(k+":"+v)
    return map

def getAllList():
    url = 'http://kanno-novel.jp/search/searchword/2/#index/4/?guid=ON&word='
    for i in range(1,199) :
        print("--------------------"+str(i))
        urlt = url.replace("#index",str(i))
        try:
            maps = getList(urlt)
            for k,v in maps.items():
                try:
                    print("download:"+k + ":" + v)
                    downOne(k,v)
                except BaseException:
                    print("error："+ k + ":" + v)

        except BaseException :
            print("列表请求失败"+str(i))

def downOne(name,url):

    object = open(name+".txt", 'w')
    index = url.replace("/viewstory/index/","").replace("/?guid=ON","")
    trueUrl = "http://kanno-novel.jp/viewstory/page/#index/#page/?guid=ON"
    trueUrl = trueUrl.replace("#index",index)
    j = 0;
    for i in range(1,10000):
        if j >10 :
            break;
        ttrueUrl = trueUrl.replace("#page",str(i))
        soup = getweb(ttrueUrl)
        strs = soup.select("#changeArea")[0].text
        #print(strs)
        if strs == '':
            j = j+1
        object.writelines(strs)
        object.flush()

#downOne('愛されている私は幸せ？',"/viewstory/index/19746/?guid=ON")


getAllList()
