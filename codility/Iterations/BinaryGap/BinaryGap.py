import math

def solution(num):
  digits = list(map(int, list('{0:b}'.format(num))))

  canCount = False
  maxGap = 0
  curGap = 0

  for idx, dig in enumerate(digits):
    if dig == 1:
      canCount = True
      if curGap > maxGap:
        maxGap = curGap
      curGap = 0
    else:
      if canCount:
        curGap += 1

  return maxGap

res = solution(561892)
# res = solution(292)
print(res)
