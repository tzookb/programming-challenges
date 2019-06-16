def solution(A, B):
  ups = []
  survived = 0

  for idx, fish in enumerate(A):
    direction = B[idx]
    if direction == 1:
      ups.append(fish)
    else:
      eaten = False
      while len(ups):
        upFish = ups.pop()
        if upFish > fish:
          ups.append(upFish)
          eaten = True
          break
        
      if not eaten:
        survived += 1
  return survived + len(ups)


fish = [4,3,2,1,5]
direction = [0,1,0,0,0]

res = solution(fish, direction)
print(res)
