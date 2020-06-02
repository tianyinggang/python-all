# 第一题：检测字符串是否为数字
s1 = '12345'
print('12345是数字：',s1.isdigit())

print(int(s1))

s2 = '12345a'
print('12345a是数字：',s2.isdigit())
print('12345a是字母数字混合形式：',s2.isalnum())
s3 = '12_345a'
print('12_345a是字母数字混合形式：',s3.isalnum())

print("     ".isspace())

print("12.45".isdecimal())  # 检测字符串中是否为整数
print("abc3d".isalpha())

# 第二题：如果将字符串转换为整数，如何做才安全
s1 = "1234"
print(int(s1))

s2 = '1234a'
#print(int(s2))

if s2.isdigit():
    print(int(s2))
else:
    print('s2不是数字，无法转换')

try:
    print(int('223aaa'))
except Exception as e:
    print('223aaa不是数字，无法转换')
    print(e)
