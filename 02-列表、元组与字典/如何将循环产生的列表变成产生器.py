a = [i for i in range(10)]
print(a)
print(type(a))
b = (i for i in range(10))
print(b)
print(type(b))
for i in a:
    print(i)

for i in b:
    print(i * i)

x = (1,2,3,4)
print(type(x))