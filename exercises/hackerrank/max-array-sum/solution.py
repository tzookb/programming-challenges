#  this one solved only 3 cases
def maxSubsetSumPartial(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    withCurrent = arr[0] + maxSubsetSum(arr[2:])
    skipCurrent = maxSubsetSum(arr[1:])
    return max(withCurrent, skipCurrent)

def maxSubsetSum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    sums = [
        arr[0],
        max(arr[0], arr[1])
    ]
    i = 2
    while i < len(arr):
        withTwoBack = arr[i] + sums[i-2]
        onlyTwoBack = sums[i-2]
        onlyOneBack = sums[i-1]
        onlyCur = arr[i]
        sums.append(
            max(withTwoBack, onlyTwoBack, onlyOneBack, onlyCur)
        )
        i += 1
    return sums[-1]


arr = []


res = maxSubsetSum(arr)
print(res)




