'''
lambda表达式：就是匿名函数，可以作为参数值传个函数或方法
'''

a = [('a',1),('b',2),('c',3),('d',4)]

a_1 = list(map(lambda x:x[0],a))
a_2 = list(map(lambda x:x[1],a))
print(a_1)
print(a_2)