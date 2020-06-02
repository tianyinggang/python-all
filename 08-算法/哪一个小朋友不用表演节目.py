def lastRemaining(n,m):
    if n < 1 or m < 1:
        return -1
    temp = 0
    for i in range(1,n+1):
        temp = (temp + m) % i
    return temp
print(lastRemaining(10,123))