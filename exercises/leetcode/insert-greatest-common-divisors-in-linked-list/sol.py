import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        cur = head.next

        while cur:
            prevNum = prev.val
            curNum = cur.val

            toInsert = ListNode(
                self.getGreatestCommonDiv(prevNum, curNum),
                cur
            )
            prev.next = toInsert

            prev = cur
            cur = cur.next
        
        return head

    def getGreatestCommonDiv(self, num1: int, num2: int) -> int:
        smaller = min(num1, num2)
        bigger = max(num1, num2)
        if bigger % smaller == 0:
            return smaller
        
        starter = smaller // 2 
        
        for num in range(starter, 0, -1):
            if smaller % num != 0:
                continue
            if bigger % num != 0:
                continue
            return num
        
        return 0
