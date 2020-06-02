# 第一题：如何快速调换字典中的key和value
d = {'a':1,'b':2}
print({v:k for k,v in d.items()})

# 第二题

a = [i*i for i in range(101)]
print(a)
