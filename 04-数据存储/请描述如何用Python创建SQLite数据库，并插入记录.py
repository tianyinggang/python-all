# 1. create table and database

import sqlite3
import os

dbPath = 'data.sqlite'
if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute('''create table persons
              (id int primary key not null,
               name text not null,
               age int not null,
               address char(100),
               salary real);''')
    conn.commit()
    conn.close()
    print('创建数据库成功')

# 2.insert
conn = sqlite3.connect(dbPath)
c = conn.cursor()
c.execute('delete from persons')
c.execute('''
insert into persons(id,name,age,address,salary)
values(1,'Bill',32,'California',20000)
''')
c.execute('''
insert into persons(id,name,age,address,salary)
values(2,'Mike',30,'Texas',10000)
''')

c.execute('''
insert into persons(id,name,age,address,salary)
values(3,'John',45,'Norway',30000)
''')
conn.commit()

print('insert success')

# 3. select

persons = c.execute('select name,age,address,salary from persons order by age')

print(type(persons))
result = []
for person in persons:
    value = {}
    value['name'] = person[0]
    value['age'] = person[1]
    value['address'] = person[2]
    result.append(value)
conn.close()
print(type(result))
print(result)

import json
resultStr = json.dumps(result)
print(resultStr)