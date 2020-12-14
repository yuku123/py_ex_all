# -- coding: utf-8 --
from selenium import webdriver
import pymysql

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名,编码格式）
db = pymysql.connect("192.168.1.103", "piday", "pidayOffice", "boss", charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
def initurl(url):
    browser = webdriver.Chrome()
    browser.get(url)

    list_result = []

    tr_list = browser.find_element_by_css_selector(".lp-table").find_elements_by_css_selector("tr")
    for tr in tr_list:
        td_str = ""
        for td in tr.find_elements_by_css_selector("td"):
            td_str = td_str + td.text + "|"
        list_result.append(td_str)

    browser.close()
    return list_result

list = []
for i in range(1,13):
    list.append(initurl('http://pta.100ppi.com/price/list---'+str(i)+'.html'))
print(list)


for lis in list:
    for s in lis:
        if len(s.split("|")) > 1:
            sql = "insert into hengyi(coo_name,price_type,price,youxiu,blank,date) values("
            for i in range(len(s.split("|"))-1):
                value = s.split("|")[i]
                if len(value)== 0:
                    value = '\'\''
                else:
                    value = '\'' +value + '\''
                sql = sql + value + ","
            sql = sql+");"
            sql = sql.replace(",)",")")
            print(sql)
            cursor.execute(sql)
            db.commit()





