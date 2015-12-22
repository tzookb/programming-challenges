def solution(A):
    seen = [False] * len(A)

    for value in A:
        if 0 < value <= len(A):
            seen[value-1] = True
 
    for idx in xrange(len(seen)):
        if seen[idx] == False:
            return idx + 1
 
    return len(A)+1
res = solution([-11,3,4,5,7])

print res