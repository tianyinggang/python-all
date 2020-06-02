import re

'''
1. 表示浮点数的正则表达式  -?\d+(\.\d+)?
2. 格式化浮点数 format
3. 如何替换原来的浮点数  sub   subn
'''
def fun(matched):
    return format(float(matched.group()),'0.2f')
result = re.subn('-?\d+(\.\d+)?',fun,'PI is 3.141592654, e is 2.71828183.  -0.2 + 1.3 = 1.1')
print(result)
print(result[0])
print(result[1])