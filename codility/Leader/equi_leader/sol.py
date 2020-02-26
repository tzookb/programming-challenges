import math

def get_dominator(A):
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
        return dominator
    else:
        return -1

def solution(A):
    dominator = get_dominator(A)
    if dominator == -1:
        return 0
    
    from_left = [1 if A[0] == dominator else 0]
    from_right = [1 if A[-1] == dominator else 0]
    for i in range(1, len(A)):
        add_if_dominator = 1 if A[i] == dominator else 0
        from_left.append(from_left[i-1] + add_if_dominator)
    A.reverse()
    for i in range(1, len(A)):
        add_if_dominator = 1 if A[i] == dominator else 0
        from_right.append(from_right[i-1] + add_if_dominator)
    from_right.reverse()
    A.reverse()

    count = 0
    for idx in range(len(from_left)-1):
        left = from_left[idx]
        right = from_right[idx+1]
        left_length = idx + 1
        right_length = len(A) - (idx + 1)
        left_min_to_dominate = math.floor(left_length/2) + 1
        right_min_to_dominate = math.floor(right_length/2) + 1

        if left >= left_min_to_dominate and \
            right >= right_min_to_dominate:
            count += 1
    return count

A = [4, 4, 2, 5, 3, 4, 4, 4]

res = solution(A)
print(res)