# 第一题：如何定义集合，集合与列表的区别

a = [1,2,3,4,5]  # 列表
print(type(a))

b = (1,2,3,4,5)  # 元组
print(type(b))

c = {1,2,3,4,5}  # 集合
print(type(c))

'''
区别：
1. 集合没有重复的元素，而列表可以有重复的元素
2. 集合中的元素与顺序无关，而列表中的元素与顺序有关
'''

a = [1,2,2,3,4,3]
print(a)
c = {1,2,2,3,4,3}
print(c)

a1 = [1,2,3]
a2 = [3,2,1]
print(a1 == a2)  # False

b1 = {1,2,3}
b2 = {3,2,1}
print(b1 == b2)  # True

# 第二题：如何去重
a = [1,2,2,3,4,3]
a_result = list(set(a))
print(a_result)
print(type(a_result))

print(tuple(set(a)))
