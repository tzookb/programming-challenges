def abbreviation(a, b):
    aIdx = bIdx = 0
    while aIdx < len(a) and bIdx < len(b):
        av = a[aIdx]
        bv = b[bIdx]
        if av.lower() == bv.lower():
            aIdx += 1
            bIdx += 1
            continue
        if av == av.lower():
            aIdx += 1
        else:
            break

    if bIdx != len(b):
        return "NO"
    for left in a[aIdx:]:
        if left.lower() != left:
            return "NO"

    return "YES"


a = "beFgH"
b = "EFG"
res = abbreviation(a, b)
print(res)




