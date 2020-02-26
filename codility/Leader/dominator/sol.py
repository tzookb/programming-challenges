import math

def solution(A):
    stack = []
    for x in A:
        if len(stack) == 0:
            stack.append(x)
            continue
        last_in_stack = stack[-1]
        if last_in_stack != x:
            stack.pop()
        else:
            stack.append(x)
    if len(stack) == 0:
        return -1

    dominator = stack[0]
    count = sum(map(lambda x : x == dominator, A))
    if count >= math.floor(len(A)/2)+1:
        return A.index(dominator)
    else:
        return -1
    

A = [3, 4, 4, 2,2,2,2,3,2]

res = solution(A)
print(res)