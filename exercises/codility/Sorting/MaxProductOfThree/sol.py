
def solution(A):
    A.sort()
    return max(
        A[-1] * A[-2] * A[-3],
        A[0] * A[1] * A[-1]
    )
    

res = solution([-3,1,2,-2,5,6])
print(res)