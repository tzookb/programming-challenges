def maximumToys(prices, k):
    money = k
    toysCount = 0
    prices.sort()
    for i in range(len(prices)):
        price = prices[i]
        if price <= money:
            toysCount += 1
            money -= price

    return toysCount

res = maximumToys([1,12,5,111,200,1000,10], 50)
print(res)
# print(getPalindromCount('aaabaa', 3))