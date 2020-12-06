def isOpener(c):
    return c in "{[("
def isBracketsMatch(open, close):
    return (
        (open == "(" and close == ")") or
        (open == "[" and close == "]") or
        (open == "{" and close == "}")
    )

def isBalanced(s):
    stack = []
    for c in s:
        if isOpener(c):
            stack.append(c)
            continue
        prev = stack.pop()
        if not isBracketsMatch(prev, c):
            return False
    if stack:
        return False
    return True

res = isBalanced("{{()()}}(")

print(res)

