import math


class FraudChecker():
    def __init__(self, withdrawls):
        self.withdrawls = withdrawls
        # self.sortedWithdrawls = withdrawls[:]
        # self.sortedWithdrawls.sort()

    def quickSelect(self, lst, k):
        if len(lst) != 0:
            pivot = lst[(len(lst)) // 2]
            smallerList = []
            for i in lst:
                if i < pivot:
                    smallerList.append(i)
            largerList = []
            for i in lst:
                if i > pivot:
                    largerList.append(i)
            count = len(lst) - len(smallerList) - len(largerList)
            m = len(smallerList)
            if k >= m and k < m + count:
                return pivot
                print(pivot)
            elif m > k:
                return self.quickSelect(smallerList, k)
            else:
                return self.quickSelect(largerList, k - m - count)

    def getMedianSorted(self, start, end):
        elms = self.sortedWithdrawls[start:end + 1]

    	length = len(elms)
    	if length % 2 == 0:
        	return (float(elms[length / 2]) + float(elms[length / 2 - 1])) / 2
    	else:
        	return elms[int(math.floor(length / 2))]

    def getMedian(self, start, end):
        elms = self.withdrawls[start:end + 1]
        length = len(elms)
        if length % 2 == 0:
            return (float(self.quickSelect(elms, length / 2)) + float(self.quickSelect(elms, length / 2 - 1))) / 2
        else:
            return self.quickSelect(elms, math.floor(length / 2))

    def calc(self, historyN):
        notifications = 0
        i = historyN
        while i < len(self.withdrawls):
        	oldWithdrawls = self.withdrawls[i - historyN:i]
        	length = len(oldWithdrawls)
        	lengthToBreak = int(length/2)+1
    		index = 0
    		while index < length:
    			if (self.withdrawls[i] >= 2 * oldWithdrawls[index]):
    				lengthToBreak -= 1
    			index += 1
    		if (lengthToBreak <= 0):
    			notifications += 1
        	i += 1
        	continue
        	median = self.getMedian(i - historyN, i - 1)
        	if (self.withdrawls[i] >= 2 * median):
        		notifications += 1
        	i += 1

        return notifications


if 0:
    n, d = map(int, raw_input().split(" "))
    withdraws = map(int, raw_input().split(" "))
    fraudChecker = FraudChecker(withdraws)
    print fraudChecker.calc(d)

else:
    elms = [1, 1, 2]
    # fraudChecker = FraudChecker([])
    # print fraudChecker.quickSelect(elms, 1)
    fraudChecker = FraudChecker([2, 3, 4, 2, 3, 6, 8, 4, 5])
    fraudChecker = FraudChecker([1,2,3,4,4])
    # print fraudChecker.getMedian(1,4)
    print fraudChecker.calc(4)
