def rotLeft(a, d):
    d = d % len(a) 
    return a[d:] + a[0:d]

print(
    rotLeft("abcde", 2)
)