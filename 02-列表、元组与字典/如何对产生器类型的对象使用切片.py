# itertools一个高效循环的迭代函数集合
from itertools import islice#islice--对迭代器做切片操作
gen = iter(range(10))
print(type(gen))

for i in islice(gen,2,6):
    print(i)