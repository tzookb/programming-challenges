import math

def solution(n):
  digits = list('{0:b}'.format(n))
  longestStreak = 0
  currentStreak = 0
  #  not countable | can count | counting
  state = 'not countable'
  for dig in digits:
    if state == 'not countable':
      if dig == '1':
        state = 'can count'
    elif state == 'can count':
      pass
    elif state == 'counting':
      pass
  pass


res = solution(989)
print(res)
