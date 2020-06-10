""" 
在Python中，迭代器是遵循迭代协议的对象。
使用iter()从任何序列对象中得到迭代器（如list, tuple, dictionary, set等）。
另一种形式的输入迭代器是generator（生成器）。
出自 https://zhuanlan.zhihu.com/p/76831058
 """
a = [i for i in range(10)]
print(a)
print(type(a)) #类型为list
b = (i for i in range(10))
print(b)
print(type(b))
""" for i in a:
    print(i)

for i in b:
    print(i * i)

x = (1,2,3,4)
print(type(x)) """