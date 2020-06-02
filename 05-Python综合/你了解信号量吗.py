'''
信号量：最古老的同步原语之一，是一个计数器。

当资源释放时，计数器就睡递增，当申请资源时，计数器就会递减

'''

from threading import BoundedSemaphore
MAX = 3

semaphore = BoundedSemaphore(MAX)

print(semaphore._value)

semaphore.acquire()

print(semaphore._value)

semaphore.acquire()

print(semaphore._value)
print(semaphore.acquire())

print(semaphore._value)

print(semaphore.acquire(False))   # 如果没有资源可以申请（_value的值是0），再次调用acquire方法，会被阻塞

print(semaphore._value)

semaphore.release()  # 第一次释放资源
print(semaphore._value)

semaphore.release()  # 第二次释放资源
print(semaphore._value)

semaphore.release()  # 第三次释放资源
print(semaphore._value)

#semaphore.release()  # 第四次释放资源，现在已经没有资源被占用，所以会抛出异常
print(semaphore._value)


