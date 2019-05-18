import math

def downToZero(n):
    return downToZeroRecursive(n, 0)

def downToZeroRecursive(n, steps):
    next_n = n
    for divider in range(2, int(math.floor(n/2)+1)):
        if n/divider == int(math.floor(n/divider)):
            max_divider = max(divider, n/divider)
            next_n = max_divider
            break
    if n == next_n:
        next_n = n - 1
    if n == 0:
        return steps
    return downToZeroRecursive(next_n, steps+1)

res = downToZero(4)
print(res)