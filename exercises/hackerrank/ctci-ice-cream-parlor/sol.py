def whatFlavors(cost, money):
    pairsDict = {}
    for idx, price in enumerate(cost):
        diff = money - price
        if diff in pairsDict:
            return print(pairsDict[diff] + 1, idx + 1)
        else:
            pairsDict[price] = idx

res = whatFlavors(
    [2, 2, 4, 3],
    4
)