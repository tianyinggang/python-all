'''
2，3，5

6

14：不是丑数


下一个丑数必定是数组中的某一个丑数A * 2、B * 3、C*5中最小的值

M2， 之前的丑数*2都小于当前最大的丑数
     之后的丑数*2都大于当前最大的丑数

M3、M5


'''

def getUglyNumber(index):
    if index < 1:
        return 0
    res = [1]
    t2 = t3 = t5 = 0
    nextdex = 1
    while nextdex < index:
        minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
        res.append(minNum)

        while res[t2] * 2 <= minNum:
            t2 += 1
        while res[t3] * 2 <= minNum:
            t3 += 1
        while res[t5] * 2 <= minNum:
            t5 += 1
        nextdex += 1
    return res[nextdex - 1]
print(getUglyNumber(100))