'''
q1

with语句适用于对资源进行访问的场合，确保不管使用过程是否发生异常都会执行必要的"清理"工作



'''

f = open('files/readme.txt','r')
data = f.read()
print(data)

'''
1. 没有关闭文件
2. 即使关闭了文件，但在关闭之前如果抛出异常，仍然会无法关闭文件
'''

f = open('files/readme.txt','r')
try:
    data = f.read()
except:
    print('抛出异常')
finally:
    f.close()


with open('files/readme.txt','r') as f:
    data = f.read()
    print(data)


'''
q2：将with语句用于自定义的类

__enter__

__exit__

'''

class MyCass:
    def __enter__(self):
        print('__enter__() is call!')
        return self
    def process1(self):
        print('process1')

    def process2(self):
        x = 1/0
        print('process2')

    def __exit__(self,exc_type,exc_value,traceback):
        print('__exit__() is call!')
        print(f'type:{exc_type}')
        print(f'value:{exc_value}')
        print(f'trace:{traceback}')

with MyCass() as my:
    my.process1()
    my.process2()