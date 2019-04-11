from pymongo import MongoClient
#建立和数据库系统的连接,指定host及port参数
client_serve = MongoClient('dds-bp170f103d9169d4-pub.mongodb.rds.aliyuncs.com:3717',
                     username='root',
                     password='funsole_411282999',
                     authSource='admin',
                     authMechanism='SCRAM-SHA-1')
serve_db_fusole = client_serve.funsole
serve_collection_recommandation_new = serve_db_fusole.recommandation_new
serve_collection_testForSearch = serve_db_fusole.testForSearch

client_local = MongoClient('192.168.1.92', 27017)
local_db_funsole = client_local.funsole
local_collection_recommandation = local_db_funsole.recommandation
local_collection_testForSearch = local_db_funsole.testForSearch

for i in local_collection_recommandation.find():
    serve_collection_recommandation_new.insert(i)

# for i in local_collection_testForSearch.find():
#     serve_collection_testForSearch.insert(i)
#



#db = client_serve.fusole
#连接表
#collection = db.fusole
#查看全部表名称
#db.collection_names()
#print(db.collection_names())
