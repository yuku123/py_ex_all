import json
from pymongo import MongoClient

file = open("sampleList.txt")

conn = MongoClient('192.168.1.92', 27017)
db = conn.funsole
recommandation = db.recommandation
i = 0;
for line in file:
    try :
        i = i+1
        json_object = json.loads(line.replace("'", '\"').replace("nan,","").replace(", nan",""))
        json_output = {}
        json_output['key'] = json_object[0]
        json_output["value"] = json_object[1]
        recommandation.insert(json_output)
    except BaseException :
        print(line)
print(i)
file.close()


