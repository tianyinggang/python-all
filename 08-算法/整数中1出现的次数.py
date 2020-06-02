def numberOfOneBetween(n):
    count = 0
    for i in range(1, n + 1):
        for i in str(i):
            if i == '1':
                count += 1
    return count
print(numberOfOneBetween(200))