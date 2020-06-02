# 题目1：编写一个函数，用于随机排列列表中的元素

a = [1,2,3,4,5,6,7, 8, 9,0 ]

import random
# 方案1
def random_list1(a):
    for i in range(0,100):
        index1 = random.randint(0, len(a) - 1)
        index2 = random.randint(0, len(a) - 1)
        a[index1],a[index2] = a[index2],a[index1]
    return a

b = random_list1(a)
print(b)

def random_list2(a):
    a_copy = a.copy()
    result = []
    count = len(a)
    for i in range(0,count):
        index = random.randint(0, len(a_copy) - 1)
        result.append(a_copy[index])
        del a_copy[index]
    return result
a = [1,2,3,4,5,6,7, 8, 9,0 ]
b = random_list2(a)
print(b)

# 第二题：
a = [1,2,3,4,5,6,7, 8, 9,0 ]
random.shuffle(a)
print(a)


