import threading
# 线程函数
def func1(s,fun):
    print('正在执行函数func1')
    fun(s)

def ff(s):
    print(f'ff输出了{s}')

t1 = threading.Thread(target=func1,args= ("hello world",ff))
t1.start()
