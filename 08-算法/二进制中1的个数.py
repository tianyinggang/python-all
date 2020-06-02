def oneNumber(n):
    print(bin(n))
    if n < 0:
        n = n & 0xffffffff
    print(bin(n))
    m = len(bin(n)) - 2
    count = 0
    '''
    1101 = 13
    
    1000   = 8 count++
    0100   = 4 count++
    0000   = 0 
    0001   = 1 count++
    
    '''
    for i in range(0,m):
        if n & 2 ** i != 0:
            count += 1
    return count

print(oneNumber(13))
print(oneNumber(-1))
