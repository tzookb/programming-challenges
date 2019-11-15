def solution(S):
    stack = []
    for l in S:
        if l == ")":
            if len(stack) == 0:
                return 0
            last = stack.pop()
            if last != "(":
                return 0
        else:
            stack.append("(")
    if len(stack) > 0:
        return 0
    return 1

# res = solution("(()(())())")
res = solution("(())")
print(res)
