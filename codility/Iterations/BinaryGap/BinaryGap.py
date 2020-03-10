def solution(num):
    digits = list(map(int, list('{0:b}'.format(num))))
    maxGap = 0
    curGap = 0

    for dig in digits:
        if dig == 1:
            if curGap > maxGap:
                maxGap = curGap
            curGap = 0
        else:
            curGap += 1
    if curGap > maxGap:
        maxGap = curGap
    return maxGap


res = solution(561892)
# res = solution(292)
# res = solution(529)
print(res)
