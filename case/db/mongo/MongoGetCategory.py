from pymongo import MongoClient

filename = 'write_data_category.txt'
fo = open(filename, "w",encoding='utf8')


conn = MongoClient('192.168.1.99', 27017)
db = conn.funsole  #连接mydb数据库，没有则自动创建
producttypes = db.producttypes #使用test_set集合，没有则自动创建

category = []

for j in range(111):

    for i in producttypes.find().skip(j*100).limit(100):


        category.append(str(i["category"]))
        #category = str(i["category"]).replace(" ", "_").replace("/", "_").replace("-", "_").split("_")

        fo.write(str(list(set(category))) + "\n")
        #fo.flush()

        print(set(category))