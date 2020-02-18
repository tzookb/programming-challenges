from functools import reduce

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = self.sumList(l1) + self.sumList(l2)
        return self.createList(total)

    def createList(self, total) -> ListNode:
        def attacher(x, y):
          x.next = y
          return y
        nodes = list(map(lambda x: ListNode(int(x)), str(total)[::-1]))
        reduce(attacher, nodes)
        return nodes[0]

    def sumList(self, l1: ListNode):
        sum = 0
        mult = 1
        item = l1

        while True:
            sum = sum + mult * item.val
            mult *= 10
            if item.next == None:
                break
            item = item.next

        return sum

sol = Solution()
print(sol.createList(135))