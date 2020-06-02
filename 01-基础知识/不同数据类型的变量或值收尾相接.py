# 字符串与字符串之间连接的方式有5种
#### 第1种：+（加号）
s1 = 'hello'
s2 = 'world'
s = s1 + s2
print(s)

### 2: 直接连接
s = "hello""world"
print(s)

### 3:用逗号（,）连接，标准输出的重定向
from io import StringIO
import sys
old_stdout = sys.stdout
result = StringIO()
sys.stdout = result
print('hello','world')
sys.stdout =old_stdout  # 恢复标准输出
result_str = result.getvalue()
print("用逗号连接：",result_str)

#####4：格式化
s = '<%s> <%s>' % (s1,s2)
print('格式化：',s)

#### 5: join
s = " ".join([s1,s2])
print("join连接：",s)

###第2题：字符串与非字符串直接如何连接
# 1：加号
n = 20
s = s1 + str(n)
print(s)
v = 12.44
b = True
print(s1 + str(n) + str(v) + str(b))

# 2: 格式化
s = '<%s> <%d> <%.2f>' %(s1,n,v)
print('格式化：',s)

# 3：重定向
from io import StringIO
import sys
old_stdout = sys.stdout
result = StringIO()
sys.stdout = result
print(s1, True, n,v,sep='*')
sys.stdout =old_stdout  # 恢复标准输出
result_str = result.getvalue()
print("用逗号连接：",result_str)

### 第3题：
class MyClass:
    def __str__(self):
        return 'This is a MyClass Instance.'

my = MyClass()
s = s1 + str(my)
print(s)