# 第1题：用逗号分隔输出的字符串
print("aa","bb",sep="中国")

# 第2题：如何让print不换行
print('hello',end='')
print('world')

# 第3题：格式化
s = 'road'
x = len(s)
print('The length of %s is %d' % (s,x))

from io import StringIO
import sys
old_stdout = sys.stdout
result = StringIO()
sys.stdout = result
print('The length of %s is %d' % (s,x))
sys.stdout = old_stdout
result_str = result.getvalue()
print('result_str',result_str,sep=':')




