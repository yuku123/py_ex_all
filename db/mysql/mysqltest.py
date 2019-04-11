# -- coding: utf-8 --

import pymysql

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名,编码格式）
db = pymysql.connect("192.168.1.103", "piday", "pidayOffice", "boss", charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "SELECT * from CityList"
# 使用 fetchone() 方法获取单条数据.
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        # 打印结果
        print("id=%s,name=%s" % \
              (id, name))
except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()