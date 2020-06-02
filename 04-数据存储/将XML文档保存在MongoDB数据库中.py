'''
q1：
NoSQL = Not Only SQL

1. 键值（key-value）数据库

Redis、Riak、Memcached

适用场景：用来存储用户信息，比如会员、配置文件、参数、购物车等。

2. 文档（Document-Oriented）数据库
MongoDB、CouchDB、RavenDB

适用场景：日志、分析数据

3. 列存储数据库
HBase、Cassandra

适用场景：日志、博客平台，。标签可以存储到一列、类别可以存储到另一列、文章可以存储在另外一列

4. 图数据库
Neo4J、OrientDB

适用场景：
（1）在一些关系型强的数据看可以使用
（2）推荐引擎

'''

'''
q2

pip install pymongo
'''

from pymongo import *

Client = MongoClient()
db = Client.data
products = db.products
products.delete_many({'price':{'$gt':0}})

import xmltodict

f = open('files/products.xml','rt',encoding='utf-8')
xml = f.read()

f.close()

print(xml)

d = xmltodict.parse(xml)
productList = d['root']['products']['product']
print(productList)

for product in productList:
    product['price'] = int(product['price'])
    productId = products.insert_one(product).inserted_id
    print(productId)

for product in products.find({'price':{'$gt':10000}}):
    print(product)


