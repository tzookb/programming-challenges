def getIdx(char):
  items = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3,
  }
  return items[char]

def get_min(arr, counters, start, end):
  last_char = arr[end]
  if last_char == "A" or ((counters[end][0] - counters[start][0]) > 0):
    return 1
  if last_char == "C" or ((counters[end][1] - counters[start][1]) > 0):
    return 2
  if last_char == "G" or ((counters[end][2] - counters[start][2]) > 0):
    return 3
  if last_char == "T" or ((counters[end][3] - counters[start][3]) > 0):
    return 4

def solution(S, P, Q):
  result = []
  counters = [[0]*4]*len(S)
  for idx, _ in enumerate(S):
    if idx == 0:
      continue
    prev_char = S[idx-1]
    curSumArr = counters[idx-1][:]
    curSumArr[getIdx(prev_char)] += 1
    counters[idx] = curSumArr

  for idx, start in enumerate(P):
    end = Q[idx]
    sol = get_min(S, counters, start, end)
    result.append(sol)
  
  return result

p = [2, 5, 0]
q = [4, 5, 6]

s = "CAGCCTA"
res = solution(s, p, q)
print(res)