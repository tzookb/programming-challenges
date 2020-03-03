results = {}

def commonChild(s1, s2):
    s1counts = {}
    s1leftover = ''
    s2counts = {}
    s2leftover = ''

    for c in s1:
        if c not in s1counts:
            s1counts[c] = 0
        s1counts[c] += 1
    for c in s2:
        if c not in s2counts:
            s2counts[c] = 0
        s2counts[c] += 1
    
    for c in s1:
        if c in s2counts:
            s2counts[c] -= 1
            s1leftover += c
            if s2counts[c] == 0:
                del s2counts[c]

    return len(s1leftover)
    # for c in s2:
    #     if c in s1counts:
    #         s1counts[c] -= 1
    #         s2leftover += c
    #         if s1counts[c] == 0:
    #             del s1counts[c]
    # print(s1leftover, s2leftover)
    


s1 = 'SHINCHAN'
s2 = 'NOHARAAA'
res = commonChild(s1, s2)
print(res)
# print(getPalindromCount('aaabaa', 3))