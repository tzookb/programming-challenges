# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

def isCloser(char):
    closers = ['}', ']', ')']
    return char in closers

def isOpener(char):
    openers = ['{', '[', '(']
    return char in openers

def isBrothers(opener, closer):
    return (opener=='{' and closer=='}') or (opener=='[' and closer==']') or (opener=='(' and closer==')')

def is_matched(str):
    stack = []
    for char in str:
        if isOpener(char):
            stack.append(char)
            continue
        if isCloser(char):
            if (len(stack)==0):
                return False
            prev = stack.pop()
            if not isBrothers(prev, char):
                return False
    return len(stack) == 0

res = is_matched('{[()](})')
print(res)