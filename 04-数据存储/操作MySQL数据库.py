'''
pymysql

pip install pymysql



'''

from pymysql import *

def connectDB():
    db = connect('127.0.0.1','root','12345678','meituan',charset='utf8')
    return db
db = connectDB()
print(type(db))

def createTable(db):
    cursor = db.cursor()
    c = db.cursor()
    try:
        c.execute('''create table persons
                      (id int primary key not null,
                       name text not null,
                       age int not null,
                       address char(100),
                       salary real);''')
        db.commit()
        return True
    except:
        db.rollback()

    return False
if createTable(db):
    print('create table success')
else:
    print('create table failed')

def insertRecords(db):
    cursor = db.cursor()
    try:
        cursor.execute('delete from persons')
        cursor.execute('''
        insert into persons(id,name,age,address,salary)
        values(1,'Bill',32,'California',20000)
        ''')
        cursor.execute('''
        insert into persons(id,name,age,address,salary)
        values(2,'Mike',30,'Texas',10000)
        ''')

        cursor.execute('''
        insert into persons(id,name,age,address,salary)
        values(3,'John',45,'Norway',30000)
        ''')
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
    return False
if insertRecords(db):
    print('成功插入记录')
else:
    print('插入记录失败')
import json
def selectRecords(db):
    cursor = db.cursor()
    sql = 'select name,age,salary from persons order by age desc'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(type(results))
    fields = ['name','age','salary']
    records = []
    for row in results:
        records.append(dict(zip(fields,row)))
    return json.dumps(records)


print(selectRecords(db))
db.close()