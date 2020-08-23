def pairs(k, arr):
    pairsDict = {}
    count = 0
    for cur in arr:
        pairsDict[cur] = True
    for cur in arr:
        diff = cur + k
        if diff in pairsDict:
            count += 1
    return count

res = pairs(
    2,
    [1,5,3,4,2]
)