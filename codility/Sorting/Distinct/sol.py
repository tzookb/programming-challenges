def solution1(A):
    A = list(dict.fromkeys(A))
    return len(A)

def solution2(A):
    mappings = {}
    for v in A:
        mappings[v] = True
    return len(mappings)

res = solution([2,1,1,2,3,1])
print(res)