# 字符串首字母大小写转换

# 第一题：修改字符串首字母的大小写

s1 = 'hello'
print(s1)
print(s1.capitalize())

# s1[0] = 'H'  只读的，会抛出异常

s1 = s1[0:1] + s1[1].upper() + s1[2:]
print(s1)

s2 = 'Hello'
s = s2[0].lower() + s2[1:]
print(s)

# 第二题：如何将字符串中每一个单词的首字母变成大写

s3 = 'hello world'
print(s3.capitalize())

arr = s3.split(' ')
new_str = f'{arr[0].capitalize()} {arr[1].capitalize()}'
print(new_str)
