'''
Python生成器（迭代）

yield

'''

def myGenerator():
    numList = [1,2,3,4,5,6,7,8]
    for num in numList:
        yield num

for num in myGenerator():
    print(num, end = ' ')
print()


'''
[[1,2,3],[4,3,2],[1,2,4,5,7]]

[1,2,3,4,3,2,1,2,4,5,7]
'''
nestedList = [[1,2,3],[4,3,2],[1,2,4,5,7]]
def enumList(nestedList):
    for subList in nestedList:
        for element in subList:
            yield element

for num in enumList(nestedList):
    print(num, end = ' ')

numList = list(enumList(nestedList))
print(type(numList))
print(numList);