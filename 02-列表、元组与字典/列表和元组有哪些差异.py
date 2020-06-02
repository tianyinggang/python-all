# 4个区别

# 1：语法差异
a = (1,2,3,4) # 元组
b = [1,2,3,4] # 列表

# 2：元组是只读的，列表是可读写的
b[1] = 3

# 3.
copy_a = tuple(a)
print(a is copy_a)  # True

copy_b = list(b)
print(b is copy_b)  # False

# 4：大小不同，元组占用的空间更小（大的内存块）

print(a.__sizeof__())
print(b.__sizeof__())
