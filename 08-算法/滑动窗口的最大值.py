def maxInWindows(num,size):
    if size <= 0 or len(num) < size:
        return []
    length = len(num)
    result = []
    for i in range(0,length - size + 1):
        result.append(max(num[i:i+size]))

    return result
print(maxInWindows([2,3,4,2,6,2,5,1],3))