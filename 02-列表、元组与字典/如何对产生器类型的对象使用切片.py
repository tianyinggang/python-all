from itertools import islice
gen = iter(range(10))
print(type(gen))

for i in islice(gen,2,6):
    print(i)