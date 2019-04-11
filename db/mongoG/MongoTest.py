# -- utf-8 --
from pymongo import MongoClient

filename = 'write_data.txt'
fo = open("res.csv", "w",encoding='utf8')


conn = MongoClient('192.168.1.99', 27017)
db = conn.funsole  #连接mydb数据库，没有则自动创建
producttypes = db.producttypes #使用test_set集合，没有则自动创建

for j in range(111):

    for i in producttypes.find().skip(j*100).limit(100):
        _id = str(i["_id"])
        tags = str(i["tags"]).split(',')
        sku = i["sku"]
        category = str(i["category"]).replace(" ", "_").replace("/", "_").replace("-", "_").split("_")
        colorway = str(i["colorway"]).replace(" ", "_").replace("/", "_").replace("-", "_").split("_")
        shortDescription = str(i["shortDescription"]).replace(" ", "_").replace("/", "_").replace("-", "_").split("_")
        title = str(i['title']).replace(" ", "_").replace("/", "_").replace("-", "_").split("_")

        category_distinct = list(set(category))
        colorway_distinct = list(set(colorway))
        shortDescription_distinct = list(set(shortDescription))
        title_distinct = list(set(title))

        fulllist = category + colorway + shortDescription + title
        fulllistdistinct = category_distinct + colorway_distinct + shortDescription_distinct + title_distinct

        fo.write(str(i["_id"]) + ","
                 + str(i["tags"]).replace(",", " ") + ","
                 + str(i["sku"]) + ","
                 + str(i["category"]) + ","
                 + str(i["colorway"]) + ","
                 + str(i["shortDescription"]) + ","
                 + str(i['title']) + ","
                 + str(fulllist).replace("[", "").replace("]", "").replace(",", " ") + ","
                 + str(fulllistdistinct).replace("[", "").replace("]", "").replace(",", " ").replace("\"", "") + ","
                 + "\n"
                 )
        fo.flush()
        print(fulllist)



