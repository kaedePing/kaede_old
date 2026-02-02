# -*- coding: utf-8 -*-
# @Time : 2022/11/2 16:30
# @Author : kaede
# @File : pymongo_study.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
#
#
# -*- Description -*-
import pymongo

# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')  # 连接数据库
db = client.kaede  # 指定数据库
collection = db.music  # 指定集合

music1 = {
    'title': '遗失的心跳',
    'singer': '萧亚轩'
}
music2 = {
    'title': '我想要',
    'singer': '咻咻满'
}
# result = collection.insert_one(music1)  # 插入数据
# print(result.inserted_id)  # 获取id

# 获取单条数据
# result = collection.find_one({'likes': '100'})
# print(result)

# 获取多条数据
results = collection.find({'singer': '萧亚轩'})
for i in results:
    print(i)

# 统计条数
count = collection.find().count()
print(count)
