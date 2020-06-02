class MyClass:
    def __init__(self):
        self.value = 0

    def __gt__(self, other):
        return self.value > other.value

    '''
    def __lt__(self, other):
        return self.value > other.value
'''

my1 = MyClass()
my1.value = 20

my2 = MyClass()
my2.value = 10

my3 = MyClass()
my3.value = 30

a = [my1,my2,my3]
print(a)

import operator


#a.sort()
a.sort(key = operator.attrgetter('value'))
b = sorted(a,key = operator.attrgetter('value'))

# 第一题：
print(a[0].value)
print(a[1].value)
print(a[2].value)
print(b[0].value)

# 第二题：降序排序
#a.sort(key = operator.attrgetter('value'),reverse=True)
a.sort()
print(a[0].value)
print(a[1].value)
print(a[2].value)
