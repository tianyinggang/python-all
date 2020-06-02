'''
threading.local

'''

import threading
import time
a = threading.local()

def worker():
    a.x = 0
    for i in range(20):
        time.sleep(0.01)
        a.x += 1
    print(threading.current_thread(),a.x)

for i in range(10):
    threading.Thread(target=worker).start()