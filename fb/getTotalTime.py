def getTotalTime(arr):
    arr.sort()
    total = 0
    while len(arr) > 1:
        cur_total = arr.pop() + arr.pop()
        total += cur_total
        arr.append(cur_total)
    return total

res = getTotalTime([2, 3, 9, 8, 4])
print(res)
