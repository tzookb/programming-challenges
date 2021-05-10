import math

def time_mult_mat_best(arr):
    result = time_mult_mat_best_recu(arr)
    return result[1]

def time_mult_mat_best_recu(arr):
    # we will assume we get non emptry arrays with 2 and above items
    if len(arr) == 2:
        return (arr, 0)
    if len(arr) == 3:
        return ([arr[0], arr[2]], arr[0] * arr[1] * arr[2])
    
    # we mult the first item
    mult_with_first_start = arr[0] * arr[1] * arr[2]
    mult_with_first_left = [arr[0]] + arr[2:]
    rest_arr_result = time_mult_mat_best_recu(mult_with_first_left)
    mult_with_first_total = mult_with_first_start + rest_arr_result[1]

    # we leave the first item to the end
    ignore_first_left = arr[1:]
    rest_with_skipped_first_result = time_mult_mat_best_recu(ignore_first_left)
    mult_with_first_last_total = arr[0] * rest_with_skipped_first_result[0][0] * rest_with_skipped_first_result[0][1] + rest_with_skipped_first_result[1]

    if mult_with_first_total < mult_with_first_last_total:
        return (rest_arr_result[0], mult_with_first_total)
    else:
        return (rest_with_skipped_first_result[0], mult_with_first_last_total)
    



tests = [
    [[100, 10, 100, 10], 20000],
    [[1,1,5,1,1], 7],
    [[1,5,1,1], 6],
    [[2,5,2,2], 6],
]

for test in tests:
    res = time_mult_mat_best(test[0])
    if res != test[1]:
        print(test)
