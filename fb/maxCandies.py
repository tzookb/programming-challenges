from heapq import heapify, heappush, heappop

def maxCandies(arr, k):
    candies_in_bags = []
    heapify(candies_in_bags)

    for count in arr:
        heappush(candies_in_bags, -1 * count)

    eaten_candies = 0

    for i in range(k):
        cur_candies = -1 * heappop(candies_in_bags)
        eaten_candies += cur_candies
        heappush(candies_in_bags, -1 * (cur_candies // 2))

    return eaten_candies



def test_code() -> None:
    # Test 1)
    maxCandies([2, 1, 7, 4, 2], 3)
    # assert maxCandies([2, 1, 7, 4, 2], 3) == 14
    # assert maxCandies([19, 78, 76, 72, 48, 8, 24, 74, 29], 3) == 228
    print("success")

if __name__ == "__main__":
    test_code()
