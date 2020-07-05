import functools

def luckBalance(k, contests):
    def cmpFunc(a, b):
        if a[0] < b[0]:
            return 1
        return -1    
    contests = sorted(contests,  key=functools.cmp_to_key(cmpFunc))

    totalLuck = 0
    skippedImportantContest = k
    for contest in contests:
        # print(contest)
        contestLuck = contest[0]
        isImportant = contest[1]
        if not isImportant:
            totalLuck += contestLuck
            continue
        if skippedImportantContest:
            totalLuck += contestLuck
            skippedImportantContest -= 1
            continue
        totalLuck -= contestLuck

    return totalLuck

k = 3 
contests = [
    [5,1],
    [2,1],
    [1,1],
    [8,1],
    [10,0],
    [5,0],
]

# 29
print(luckBalance(k, contests))