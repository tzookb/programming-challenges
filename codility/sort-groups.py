import math

def solution(A):
  totalGroups = 0
  idx = 0

  while idx < len(A):
    minVal = A[idx]
    endIdx = idx
    bidx = idx + 1

    while bidx < len(A):
      nextVal = A[bidx]
      if nextVal < minVal:
        endIdx = bidx
        minVal = nextVal
      bidx +=1

    totalGroups +=1

    if idx == endIdx:
      idx += 1
    else:
      idx = endIdx + 1
  
  return totalGroups

res = solution([2,4,1,6,5,9,7])
print(res)
