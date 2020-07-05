def firstNotRepeatingCharacter(s):
    occur = {}
    singles = {}
    stack = []
    for c in s:
        if c not in occur:
            occur[c] = 0
        occur[c] += 1

    for occurItem in occur:
        if occur[occurItem] == 1:
            singles[occurItem] = True
    
    for c in s:
        if c in singles:
            return c

    return "_"

print(firstNotRepeatingCharacter("abacabad"))


# TODO https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC