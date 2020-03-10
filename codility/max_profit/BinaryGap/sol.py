def solution(prices):
    if not prices:
        return 0
    purchase = prices[0]
    profit = 0
    for p in prices:
        if p < purchase:
            purchase = p
        if p > purchase:
            curProfit = p - purchase
            if curProfit > profit:
                profit = curProfit

    return profit

prices = [3,2,3]
res = solution(prices)
print(res)
