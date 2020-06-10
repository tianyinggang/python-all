# q1
'''
match：用于匹配
search：用于搜索

'''

import re
m1 = re.match('.*python','I love python')#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(m1)
m2 = re.search('python','I love python')
print(m2)

# q2

m = re.search('1\d{10}','我的手机号是：18612345678')
if m is not None:
    print(m.group())
    print(m.start())
    print(m.end())