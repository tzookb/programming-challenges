def getMilestoneDays(revenues, milestones):
    total = 0
    mile_idx = 0
    wins = {}
    same_mls = milestones.copy()
    milestones.sort()
    for i, v in enumerate(revenues):
        total += v
        if mile_idx >= len(milestones):
            break
        while mile_idx < len(milestones) and total >= milestones[mile_idx]:
            wins[milestones[mile_idx]] = i + 1
            mile_idx += 1
    
    wins_arr = []
    for mls in same_mls:
        wins_arr.append(wins[mls])
    return wins_arr

revenues = [100, 200, 300, 400, 500]
milestones = [300, 800, 1000, 1400]
res = getMilestoneDays(revenues, milestones)
print(res)
