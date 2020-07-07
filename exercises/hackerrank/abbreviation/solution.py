def abbrev(a, b):
    if len(a) + len(b) == 0:
        return True
    if len(a) == 0 and len(b) > 0:
        return False
    if len(a) > 0 and len(b) == 0:
        if a[0].isupper():
            return False
        return abbrev(a[1:], b)

    av = a[0]
    bv = b[0]

    if av.islower():
        removeFromA = abbrev(a[1:], b)
        capitalFromA = av.upper() == bv and abbrev(a[1:], b[1:])

        return removeFromA or capitalFromA

    if av.isupper() and av == bv:
        return abbrev(a[1:], b[1:]) 

    return False

def abbreviation(a, b):
    if abbrev(a, b):
        return "YES"
    return "NO"

a = "LLlllLLL"
b = "LLLL"
res = abbreviation(a, b)
print(res)