import math

def solution(A):
  A.sort()
  arr = list(dict.fromkeys(A))
  nextItem = 1
  for a in arr:
    if a > 0:
      print(nextItem, a)
      if nextItem == a:
        nextItem += 1
      else:
        return nextItem


res = solution([1, 3, 6, 4, 1, 2])
print(res)
