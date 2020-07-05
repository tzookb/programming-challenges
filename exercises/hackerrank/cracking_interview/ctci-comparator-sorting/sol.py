def comparator(a, b):
    if a.score > b.score:
        return -1
    elif a.score == b.score:
        if a.name <= b.name:
            return -1
        else:
            return 1
    else:
        return 1

a = 1
b = 1
res = comparator(a, b)
print(res)
# print(getPalindromCount('aaabaa', 3))