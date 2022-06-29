from typing import List

def createBin(size):
    num = 2**size - 1
    binned = bin(num)
    res = [int(d) for d in str(binned)[2:]]
    return res


print(createBin(5))
# coins = [1]
# amount = 0
# s = Solution()
# res = s.coinChange(coins, amount)
# print(res)