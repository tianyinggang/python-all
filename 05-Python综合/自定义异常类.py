'''
Exception

'''

class MyException(Exception):
    pass

num = 50
try:
    if num >= 10:
        raise MyException('抛出异常')
    print('正常执行代码')
except MyException:
    print('发生了异常')