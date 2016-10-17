def candy(machines, workers, price, cash, goal, steps, isBuyStep):
    if cash >= goal:
        if not isBuyStep:
            return steps
    
    if cash < price:
        return candy(machines, workers, price, cash+machines*workers, goal, steps+1, False)

    if machines < workers:
        if workers > price:
            return candy(machines+1, workers, price, cash-price, goal, steps, True)
        else:
            return candy(machines, workers, price, cash+machines*workers, goal, steps+1, False)
    else:
        if machines > price:
            return candy(machines, workers+1, price, cash-price, goal, steps, True)
        else:
            return candy(machines, workers, price, cash+machines*workers, goal, steps+1, False)


if 1:
    print candy(3, 1, 2, 0, 12, 0, False)
else:
    machines, workers, price, goal = map(int, raw_input().split(" "))
    print candy(machines, workers, price, 0, goal, 0, False)