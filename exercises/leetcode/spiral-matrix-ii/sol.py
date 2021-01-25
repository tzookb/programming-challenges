from typing import List

class Solution:
    def generateBlankArr(self, n: int) -> List[List[int]]:
        grid = []
        for _ in range(n):
            row = [0] * n
            grid.append(row)
        return grid

    def print(self, grid):
        for row in grid:
            print(row)
        print("---------")

    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = self.generateBlankArr(n)
        steps = {
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
            "up": (-1, 0)
        }
        limits = {"left": 0, "up": 1, "right": n-1, "down": n-1}
        direction = "right"
        step = 1
        cur = [0, 0]

        while step <= n**2:
            arr[cur[0]][cur[1]] = step
            if direction == "right" and cur[1] == limits["right"]:
                direction = "down"
                limits["right"]-= 1

            elif direction == "down" and cur[0] == limits["down"]:
                direction = "left"
                limits["down"] -= 1

            elif direction == "left" and cur[1] == limits["left"]:
                direction = "up"
                limits["left"] += 1

            elif direction == "up" and cur[0] == limits["up"]:
                direction = "right"
                limits["up"] += 1

            cur[0] += steps[direction][0]
            cur[1] += steps[direction][1]

            step += 1
        return arr