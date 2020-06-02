# 2  fstring

name = 'Bill'
age = 20

def getAge():
    return 21

s = f"我是{name}，我今年{age}岁，明年{getAge()}岁"

print(s)

class Person:
    def __init__(self):
        self.name = 'Mike'
        self.age = 40
    def getAge(self):
        return 41

person = Person()

s1 = f"我是{person.name}，我今年{person.age}岁，明年{person.getAge()}岁"
print(s1)



