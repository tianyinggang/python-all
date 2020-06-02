# 第一题：*和**的作用

# 单星（*）
# 以元组形式导入
# 可变参数
# 如果可变参数不是最后一个参数，那么为可变参数后面的形参指定参数值，必须用命名参数
def fun1(param1, *param2,x):
    print('param1:',param1)
    print('param2:',param2,type(param2))
    print('x:',x)

fun1(1,2,3,4,5,x = 6)

# 双星号（**）
# 以字典形式导入 key 和  value
def fun2(param1, **param2):
    print('param1:',param1)
    print('param2:',param2,type(param2))
fun2(1,a = 2,b = 3,c = 4,d = 5)

# 第2题：如何合并列表和字典

# 列表
a = [1,2,3]
b = [4,5,6]

# 1
c = a + b
print(c)

# 2
a.extend(b)
print(a)

a = [1,2,3]
b = [4,5,6]

# 3
# [[1, 2, 3], [4, 5, 6]]
# [1,2,3,4,5,6]
x = [a,b]
print(x)
x = [*a, *b]
print(x)

# 字典
a = {'A':1,'B':2}
b = {'C':3,'D':4}
# c = {'A':1,'B':2,'C':3,'B':4}
c = {**a,**b}
print(c)

