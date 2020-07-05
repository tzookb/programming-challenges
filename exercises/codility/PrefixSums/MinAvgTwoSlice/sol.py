def solution(A):
    minVal = 10001
    minIdx = 0
    i = 0
    while i < len(A)-1:
        first = A[i]
        sec = A[i+1]
        avg = float(first+sec) / float(2)
        if avg < minVal:
            minVal = avg
            minIdx = i
        if i < len(A)-2:
            # size 3 check
            third = A[i+2]
            avg = float(first+sec+third) / float(3)
            if avg < minVal:
                minVal = avg
                minIdx = i
        i += 1
    return minIdx


res = solution([4, 2, 2, 5, 1, 5, 8])
print(res)
