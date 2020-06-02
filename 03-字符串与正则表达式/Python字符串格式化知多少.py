# 1：格式化字符串的方式
'''
1. %格式化
2. 模板字符串
3. 字符串的format方法
4. fstring

'''

# 通过Template对象封装  $放置一些占位符，并通过substitute方法用实际的值替换这些占位符

from string import Template

template1 = Template('$s是我最喜欢的编程语言，$s非常容易学习，而且功能强大')
print(template1.substitute(s = 'Python'))
print(template1.substitute(s = 'PHP'))

template2 = Template('${h}ello world')
print(template2.substitute(h = 'abc'))

template3 = Template('$dollar$$相当于多少$pounds英镑')
print(template3.substitute(dollar=20,pounds=16))

data = {}
data['dollar'] = 30
data['pounds'] = 25

print(template3.substitute(data))



