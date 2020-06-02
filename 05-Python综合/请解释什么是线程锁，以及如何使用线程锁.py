'''
线程锁：目的是将一段代码锁住，一旦获得锁权限，除非释放线程锁，否则其他任何代码都无法获得锁权限

为什么需要线程锁

由于多线程同时在完成特定的操作时，由于并不是原子操作，所以在完成操作的过程中可能会被打断，去做其他的操作。

可能会产生脏数据

例如，一个线程读取变量n【初始值是0】，然后n++，最后输出n

当访问n++后，被打断，由另外的线程做同样的工作，这时n被加了2次，所以n最后等于2，而不是1




'''
from atexit import register
from threading import Thread,Lock,currentThread
from time import sleep,ctime
import random
lock = Lock()
print(type(lock))

def fun():
    lock.acquire()  # 加锁
    for i in range(5):
        print('Thread Name','=',currentThread().name,'i','=',i)
        sleep(random.randint(1,5))
    lock.release() # 解锁
def main():
    for i in range(3):
        Thread(target=fun).start()
@register
def exit():
    print('线程执行完毕：',ctime())
main()