# 第1题：用逗号分隔输出的字符串
# sep 将值放入两者中间 
print("aa","bb",sep="中国")

# 第2题：如何让print不换行
print('hello',end='')
print('world')

# 第3题：格式化
s = 'road'
x = len(s)
print('The length of %s is %d' % (s,x)) 

# StringIO用于像文件一样对字符串缓冲区或者叫做内存文件进行读写。
from io import StringIO

import sys #该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数
old_stdout = sys.stdout
result = StringIO()#引用内存中的字符串 s='road'
sys.stdout = result#sys.stdout是print的一种默认输出格式，等于print "%VALUE%"
print('The length of %s is %d' % (s,x))
sys.stdout = old_stdout
result_str = result.getvalue()
print('result_str',result_str,sep=':')




