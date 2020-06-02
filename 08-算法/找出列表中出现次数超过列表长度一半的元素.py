def moreThanHalfNum(numbers):
    d = {}
    maxNum = 'no'
    listCount = len(numbers)

    for n in numbers:
        if d.get(n) is None:
            d[n] = 1
            if maxNum == 'no':
                maxNum = n
        else:
            d[n] += 1
        if n != maxNum and d.get(n) > d.get(maxNum):
            maxNum = n
        if d.get(maxNum) > listCount // 2:
            return maxNum
    return 'no'
print(moreThanHalfNum([1,1,4,2,2,0,0,0,3,5,3,2,1,1,1,1,1,1]))
