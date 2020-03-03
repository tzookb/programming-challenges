import math
import statistics

def activityNotifications(expenditure, d):
    notifications = 0
    totalDays = len(expenditure)
    pastExpenditure = expenditure[0:d]

    for i in range(d, totalDays):
        
        median = statistics.median(pastExpenditure)

        cur = expenditure[i]
        if cur >= median*2:
            notifications += 1
    return notifications

expenditure = [2,3,4,2,3,6,8,4,5]
d = 5
res = activityNotifications(expenditure, d)
print(res)
# print(getPalindromCount('aaabaa', 3))