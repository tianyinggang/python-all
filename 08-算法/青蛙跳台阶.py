'''
前提：青蛙一次只能跳1级或2级台阶

n   f(m)

假设第1次跳1级台阶 f(n-1)
假设第1次跳2级台阶 f(n-2)

f(n) = f(n-1) + f(n-2)


f(1) = 1
f(2) = 2


'''

def jumpFloor(number):
    res = [1,2]
    while len(res) <= number:
        res.append(res[-1] + res[-2])
    if number == 1:
        return 1
    else:
        return res[number - 1]

print(jumpFloor(20))