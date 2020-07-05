def countSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    print("Array is sorted in {:d} swaps.".format(swaps))
    print("First Element: {:d}".format(arr[0]))
    print("Last Element: {:d}".format(arr[-1]))

res = countSwaps([3,2,1])
print(res)
# print(getPalindromCount('aaabaa', 3))