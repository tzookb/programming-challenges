from typing import List

def minimalHeaviestSetRecu(arr, min_sum, elements_needed, a_group):
    if elements_needed < 0:
        return []
    
    if elements_needed == 0:
        if sum(a_group) > min_sum:
            # print("asdasds")
            # print(a_group, min_sum)
            return [a_group]
        return []

    results = []
    for i in range(len(arr)):
        chosen = arr[i]
        left_arr = arr[0:i]
        right_arr = arr[i+1:0]
        next_arr = left_arr + right_arr

        temp_results = minimalHeaviestSetRecu(next_arr, min_sum, elements_needed - 1, a_group + [chosen])
        results += temp_results

    return results
            



def minimalHeaviestSetA(arr):
    arr.sort(reverse=True)
    total = sum(arr)
    min_sum = total // 2 + 1

    for size in range(1, len(arr)):
        results = minimalHeaviestSetRecu(arr, min_sum, size, [])
        if results:
            return results[0]
            break
    return -1

# ar = [3,7,5,6,2]
ar = [5,3,2,4,1]
ar = [6,5,4,2,1]
ar = [6,5,3,2,4,1,2]
res = minimalHeaviestSetA(ar)
print(res)