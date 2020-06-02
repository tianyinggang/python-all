
'''
nums = [1, 2, -2,-1, 5, -4]


i = 3，j = 5

mul(i,j) = mul(0,j) / mul(0,i)

0： 需要重新开始
< 0 ：应该找到前面最大的负数
> 0： 最小的正数



'''

def maxMul(nums):
    if not nums:return
    # 目前的累乘
    cur_mul = 1

    # 前面最小的正数
    min_pos = 1

    # 前面最大的负数
    max_neg = float("-inf")
    # 结果
    result = float("-inf")

    for num in nums:
        cur_mul *= num

        if cur_mul > 0:
            result = max(result, cur_mul // min_pos)
            min_pos = min(min_pos,cur_mul)
        elif cur_mul < 0:
            if max_neg != float("-inf"):
                result = max(result,cur_mul // max_neg )
            else:
                result = max(result,num)
            max_neg = max(max_neg,cur_mul)
        else:
            cur_mul = 1
            min_pos = 1
            max_neg = float("-inf")
            result = max(result,num)
    return result

data = [1,2,-2,0,5,-4]
print(maxMul(data))
data = [1, 2, -2,-1, 5, -4]
print(maxMul(data))


