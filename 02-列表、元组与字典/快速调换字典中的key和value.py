# 第一题：如何快速调换字典中的key和value
d = {'a':1,'b':2}
print({v:k for k,v in d.items()})#   以列表返回可遍历的(键, 值) 元组数组。返回{1: 'a', 2: 'b'}

# 第二题

a = [i*i for i in range(101)]
print(a)
