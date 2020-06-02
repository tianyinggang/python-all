'''

协程：又称为微线程、纤程，英文名：Coroutine

通过async/await语法进行生命，是编写异步应用的推荐方式

import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())

1. run
2. create_task
'''


import asyncio
import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def myfun():
    print(f'开始时间：{time.strftime("%X")}')
    await say_after(1, 'hello')
    await say_after(2,'world')

    print(f"执行完成：{time.strftime('%X')}")
asyncio.run(myfun())


'''
create_task
'''


async def myfun1():
    task1 = asyncio.create_task(
        say_after(1, 'hello')
    )
    task2 = asyncio.create_task(
        say_after(2, 'world')

    )

    print(f'开始时间：{time.strftime("%X")}')

    await task1
    await task2

    print(f'介绍时间：{time.strftime("%X")}')
asyncio.run(myfun1())