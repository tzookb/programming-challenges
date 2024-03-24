def icecreamParlor(m, arr):
    prev = {}
    for i, n in enumerate(arr):
        diff = m - n
        if diff in prev:
            return [prev[diff] + 1, i + 1]
        prev[n] = i

    return [-1, -1]

res = icecreamParlor(6, [1,3,4,5,6])
print(res)