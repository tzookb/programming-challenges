def selection_sort(arr):
    for i, _ in enumerate(arr):
        minidx = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[minidx]:
                minidx = j
            j += 1

        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr

arr = [3,5,1,7,4,2]
sorted_arr = selection_sort(arr)
print(sorted_arr)