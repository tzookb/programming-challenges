from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        going_left = []
        right_asteroids = []
        for asteroid in asteroids:
            if asteroid > 0:
                going_left.append(asteroid)
                continue

            right_asteroid_saved = True
            while going_left:
                first_left = going_left.pop()
                if first_left > abs(asteroid):
                    going_left.append(first_left)
                    right_asteroid_saved = False
                    break
                elif first_left == abs(asteroid):
                    right_asteroid_saved = False
                    break
                else:
                    # left explodes by right
                    pass
            if right_asteroid_saved:
                right_asteroids.append(asteroid)
        
        return right_asteroids + going_left

nums = [-2,-1,1,2]
s = Solution()

res = s.asteroidCollision(nums)

print(res)
