from typing import List


def countTriplets(arr, sum):
    results = []
    n = len(arr)

    for i in range(0, n - 2):
        j = i + 1
        k = n - 1

        while(j < k):
            if (arr[i]+arr[j]+arr[k] >= sum):
                k = k-1
            else:
                results.append([arr[i], arr[j], arr[k]])
                j = j+1

    return results


nums = [-2, 0, 1, 3]
target = 2
# s = Solution()
# res = s.threeSumSmaller(nums, target)
res = countTriplets(nums, target)
# res = s.twoSumSmaller(nums, target)
# res = s.getAllPairs(nums)
print(res)
