def leftRotateString(s,k):
    return s[k:] + s[:k]
print(leftRotateString("abcXYZdef",3))

def rightRotateString(s,k):
    return s[len(s) - k:] + s[:len(s)-k]
print(rightRotateString("abcXYZdef",3))
