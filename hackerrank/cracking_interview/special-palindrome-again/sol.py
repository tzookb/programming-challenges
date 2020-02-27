def getPalindromCount(s, startLen):
    count = 0
    startItems = s[0:startLen]
    endingItems = s[startLen+1:]
    for a,b in zip(startItems, endingItems):
        if a != b:
            break
        count += 1
    return count

def substrCount(n, s):
    count = len(s)

    prev = None
    tail = ''
    for idx, c in enumerate(s):
        if prev == c:
            tail = tail + c
        else:
            tail_size = len(tail)
            count += (tail_size-1)*tail_size/2
            start_str = idx - len(tail)
            end_str = idx + 1 + len(tail)
            to_check_str = s[start_str:end_str]
            if len(to_check_str) > 2:
                count += getPalindromCount(to_check_str, len(tail))
            tail = c
            prev = c
    
    tail_size = len(tail)
    count += (tail_size-1)*tail_size/2
    return int(count)

n = 5
str = 'asasd'
res = substrCount(n, str)
print(res)
# print(getPalindromCount('aaabaa', 3))