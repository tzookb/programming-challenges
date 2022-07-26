from typing import List



def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    def getDist(size, cur, next):
        dists = []
        if cur < next:
            # left to right
            dists.append(next - cur)
            # right to left
            d = cur + size - next
            dists.append(d)
        else:
            # right to left
            dists.append(cur - next)
            # left to right
            d = size - cur + next
            dists.append(d)
        min_dist = min(dists)
        return min_dist

    cur = 1
    total = 0
    for num in C:
        cur_dist = getDist(N, cur - 1, num - 1)
        total += cur_dist
        cur = num

    return total

# [1,2,3,4,5]

res = getMinCodeEntryTime(3, 3, [1, 2, 3])
# res = getMinCodeEntryTime(10, 4, [9, 4, 4, 8])
print(res)