# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.buildListFromNum(
            self.getLinkedNum(l1) + self.getLinkedNum(l2)
        )
    
    def getLinkedNum(self, l: Optional[ListNode], ) -> int:
        total = 0
        cur = l
        while cur:
            total *= 10
            total += cur.val
            cur = cur.next
        
        return total
    
    def buildListFromNum(self, num: int) -> Optional[ListNode]:
        if num == 0:
            return ListNode(0, None)
        prev = None
        while num:
            digit = num % 10
            num = num // 10
            node = ListNode(digit, prev)
            prev = node
        return prev
        