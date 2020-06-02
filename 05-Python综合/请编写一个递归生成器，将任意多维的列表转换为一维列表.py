'''


'''

nestedList = [4,[1,2,[3,5,6]],[4,3,[1,2,[4,5]],2],[1,2,4,5,7]]
print(nestedList)

def enumList(nestedList):
    try:
        for subList in nestedList:
            for element in enumList(subList):
                yield element
    except TypeError:
        yield nestedList   # 迭代单个值

for num in enumList(nestedList):
    print(num, end=' ')
print(list(enumList(nestedList)))