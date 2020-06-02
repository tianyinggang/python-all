# 第一题：添加和删除集合中的元素
x = {3,2,1}
x.add(123)
print(x)
x.add(1)
print(x)
x.add('abc')
print(x)

x.remove(123)
if x.__contains__(444):
    x.remove(444)
else:
    print('444在集合中不存在')

# 第2题：集合之间的运算

x1 = {1,2,3}
x2 = {3,4,5}
print('x1和x2合并：',x1 | x2) # 集合之间的合并
print('x1和x2合并：',x1.union(x2))

print('x1和x2相交：', x1 & x2)  # 集合之间的相交
print('x1和x2相交：', x1.intersection(x2))

print(x1.difference(x2))  # 将x1中有的，在x2中也有的删除，返回值是x1的子集合

print(x1 ^ x2)  # 刨除x1和x2共用的元素，返回值是集合并的子集