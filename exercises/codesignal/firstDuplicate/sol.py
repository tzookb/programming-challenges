def firstDuplicate(a):
    occur = {}
    for v in a:
        if v in occur:
            return v
        occur[v] = True
    return -1

firstDuplicate([2, 1, 3, 5, 3, 2])