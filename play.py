from typing import List
from collections import Counter

class Window:
    def __init__(self, arr):
        self.counts = Counter()

        self.max_val = 0
        self.min_val = float("inf")

        for x in arr:
            self.add(x)

    def getDiff(self):
        return self.max_val - self.min_val

    def add(self, item):
        if item not in self.counts:
            self.max_val = max(self.max_val, item)
            self.min_val = min(self.min_val, item)

        self.counts[item] += 1

    def remove(self, item):
        if item not in self.counts:
            return

        if self.counts[item] > 1:
            self.counts[item] -= 1
            return

        del self.counts[item]

        if item == self.max_val:
            self.max_val = self._getMax()

        if item == self.min_val:
            self.min_val = self._getMin()

    def _getMax(self):
        items = self.counts.keys()
        if items:
            return max(items)
        return 0

    def _getMin(self):
        items = self.counts.keys()
        if items:
            return min(items)
        return 0

    def print(self):
        print(self.counts)
        print(self.max_val)
        print(self.min_val)




def getTotalImbalancesForWindow(weight, size):
    length = len(weight)
    total_windows = length - size + 1
    left = 0
    right = size - 1
    counter = 0
    imbalances = 0

    window = Window(weight[left:right+1])
    while counter < total_windows:
        diff = window.getDiff()
        imbalances += diff

        # window.print()

        counter += 1
        if counter >= total_windows:
            break

        left_val = weight[left]
        left += 1
        right += 1
        right_val = weight[right]
        window.remove(left_val)
        window.add(right_val)

    return imbalances

def getTotalImbalance(weight):
    imbalances = 0
    window_size = 2
    shipments_count = len(weight)
    if shipments_count < 2:
        return 0

    while window_size <= shipments_count:
        cur_imbalance = getTotalImbalancesForWindow(weight, window_size)
        imbalances += cur_imbalance

        window_size += 1

    return imbalances


res = getTotalImbalance([1,2,3])
# res = getTotalImbalancesForWindow([1,2,3],2)
print(res)

