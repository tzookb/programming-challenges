
def count_subarrays(arr):
    size = len(arr)

    # from left
    fromLeft = [0] * size
    for i, x in enumerate(arr):
        j = i
        log = False
        while j >= 0:
            cur = arr[j]
            if cur <= x:
                fromLeft[i] += 1
            else:
                break
            j -= 1
    
    # from left
    fromRight = [0] * size
    for i in range(size-1, -1, -1):
        x = arr[i]
        j = i
        log = False
        while j < size:
            cur = arr[j]
            if cur <= x:
                fromRight[i] += 1
            else:
                break
            j += 1

    both = [x + y - 1 for (x, y) in zip(fromLeft, fromRight)]
    
    return both



test_1 = [3, 4, 1, 6, 2]
expected_1 = [1, 3, 1, 5, 1]
output_1 = count_subarrays(test_1)

print(output_1)
print(expected_1 == output_1)
