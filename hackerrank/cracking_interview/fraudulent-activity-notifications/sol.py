import math
import statistics
import bisect


class SortedArray():
    def __init__(self, array):
        self.array = sorted(array)

    def add(self, x):
        # Assumes array is sorted, and keeps it sorted
        bisect.insort(self.array, x)

    def remove(self, x):
        # Assumes array is sorted, and keeps it sorted
        del self.array[bisect.bisect_left(self.array, x)]

    def median(self):
        return statistics.median(self.array)


def activityNotifications(expenditure, d):
    notifications = 0
    totalDays = len(expenditure)
    pastExpenditure = expenditure[0:d]

    sa = SortedArray(pastExpenditure)
    for i in range(d, totalDays):
        cur = expenditure[i]
        median = sa.median()
        if cur >= median*2:
            notifications += 1
        
        toRemove = expenditure[i-d]
        sa.remove(toRemove)
        sa.add(cur)
    return notifications


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
res = activityNotifications(expenditure, d)
print(res)
# print(getPalindromCount('aaabaa', 3))
