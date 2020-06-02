# q1
f= open('./files/readme.txt','r')
print(type(f))
#print(f.read())

# q2：read、readline、readlines

# read：读取文件的全部内容
#print(f.read())
print(f.read(3))  # 如果指定参数n，会读取前n个字符

f.seek(6)
print(f.read(2))

f.close()

# readline
f= open('./files/readme.txt','r')
print('------------')
#print(f.readline())
#print(f.readline())
print(f.readline(20))  # 如果指定n，当n比当前行字符个数小，读取当前行前n个字符，如果超过当前行字符个数，那么最多读取当前行的内容

f.close()

# readlines
f= open('./files/readme.txt','r')
print('------------')
#print(f.readlines())
#print(f.readlines(3)) # 如果指定n，那么只会读取行字符个数之和大于n的行
print(f.readlines(12))
f.close()





