def solution(A):
    max_sum = A[0]
    temp_sum = 0

    for val in A:
        temp_sum += val
        if temp_sum > max_sum:
            max_sum = temp_sum

        if temp_sum < 0:
            temp_sum = 0

    return max_sum
    

# res = solution([3,2,-6,4,0])
res = solution([-6,-2,-1])
# res = solution([-1,1])
print(res)