'''
q1：递归

'''

def rectCover1(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return rectCover1(number - 1) + rectCover1(number - 2)
print(rectCover1(12))

'''
非递归
'''

def rectCover2(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        res = [0,1,2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]
print(rectCover2(12))