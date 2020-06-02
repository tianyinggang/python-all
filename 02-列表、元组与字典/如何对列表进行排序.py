# 第一题：排序列表的方法
a = [5,4,2,7,3,8,3]
a.sort()
print(a)

b = [6,4,3,3,76,2,234]
c = sorted(b)
print(c)
# 第二题：sort和sorted的区别
'''
1. sort属于列表，sorted是独立的函数
2. sort改变列表本身，sorted返回一个排好序的列表副本
'''
print(c == b)

# 第三题：降序排列
a.sort(reverse=True)
print(a)

print(sorted(b,reverse=True))



