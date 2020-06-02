'''
hasattr：可以判断一个对象是否包含某个属性
getattr：可以获取对象中某一个属性的值
setattr：可以设置对象中某一个属性的值

'''

class Person():
    def __init__(self):
        self.name = 'lining'
        self.age = 12
    def show(self):
        print(self.name)
        print(self.age)

if hasattr(Person,'show'):
    print('存在show方法')

person = Person()
setattr(person,'sex','男')
setattr(person,'age',21)
print(getattr(person,'sex'))
print(getattr(person,'age'))
print(getattr(person,'name'))

person.show()