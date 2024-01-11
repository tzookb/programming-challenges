from typing import List, Dict, Tuple
class Solution:
    def calcTimeForArrival(self, target: int, position: int, speed: int) -> int:
        return 

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        stacked = []
        for car in cars:
            dest_time = (target - car[0]) / car[1]
            stacked.append(dest_time)
            
            if len(stacked) <= 1:
                continue

            if stacked[-1] <= stacked[-2]:
                stacked.pop()

        return len(stacked)



s = Solution()

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
res = s.carFleet(target, position, speed)

print(res)

