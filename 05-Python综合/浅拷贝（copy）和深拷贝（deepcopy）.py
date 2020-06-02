'''
copy：只复制深层对象的引用
deepcopy：复制深层对象本身

'''

import copy
a = [1,2,3,4,['a','b']]

c = copy.copy(a) # 浅拷贝

d = copy.deepcopy(a) # 深拷贝
print(c)
print(d)

a.append(5)
print(a)
print(c)
print(d)

a[4][0] = 'x'
print('-------------')
print(a)
print(c)
print(d)



