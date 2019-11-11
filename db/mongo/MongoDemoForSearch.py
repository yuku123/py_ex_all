# -- utf-8 --
from pymongo import MongoClient

##---------------------function-define----------------------

def getStringOfKeyWord(i):
    try:
        brand=str(i['brand'])
    except BaseException:
        brand=''

    try:
        category = str(i['category'])
    except BaseException:
        category=''

    try:
        gender = str(i['gender'])
    except BaseException:
        gender=''

    try:
        shortDescription = str(i['shortDescription'])
    except BaseException:
        shortDescription=''

    try:
        title = str(i['title'])
    except BaseException:
        title=''

    try:
        tags = str(i['tags'])
    except BaseException:
        tags=''

    string_raw = brand + " "+ category+ " "+ gender+ " "+ shortDescription+ " "+ title+ " "+ tags
    string_raw = string_raw.replace("\"","").replace(","," ").replace("-"," ").replace("_"," ").replace("(","").replace(")","")

    # list_distinct=list(set(string_raw.split(" ")))
    #
    # string_raw_distinct = ''
    # for s in list_distinct:
    #     string_raw_distinct = string_raw_distinct + s + " "

    return string_raw
##---------------------function-define----------------------

conn = MongoClient('192.168.1.120', 27017)
db = conn.funsole  #连接mydb数据库，没有则自动创建
producttypes = db.producttypes #使用test_set集合，没有则自动创建

for i in producttypes.find():
    ##获得sku的部分
    sku = i['sku']
    ##此处需要对该文本的所有字符可能性进行拆解，得到一个包含所有search可能性的list
    string_raw = getStringOfKeyWord(i)
    i['search_key']=string_raw
   #print(i)
    #print(string_raw)
    testForSearch=db.testForSearch
    testForSearch.insert(i)

