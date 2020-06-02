# 第一题：连接列表有两种方式：+和extend，元组只有一种：+
a = [1,5,7,9,6]
b = [2,3,3,6,8]
c = (1,2,3)
d = (2,3,3,4)
print(a + b)
print(c + d)
a.extend(b)
print(a)



# 第二题：差异
'''
1. +不会改变参与连接的列表的值，但extend方法可以改变a列表的值
2. +两侧要么都是元组，要么都是列表。但是列表的extend方法可以将一个元组添加列表后面
'''

a.extend(c)
print(a)

#print(a + c)
print(c + d)
