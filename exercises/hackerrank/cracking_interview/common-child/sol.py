results = {}

def commonChild(s1, s2):
    if len(s1) * len(s2) == 0:
        return 0

    key = s1 + s2
    if key in results:
        return results[key]

    if s1[-1] == s2[-1]:
        res = 1 + commonChild(s1[0:-1], s2[0:-1])
    else:
        res = max(commonChild(s1, s2[0:-1]), commonChild(s1[0:-1], s2))
    
    results[key] = res
    return res


s1 = 'HARRY'
s2 = 'SALLY'
res = commonChild(s1, s2)
print(res)
# print(getPalindromCount('aaabaa', 3))