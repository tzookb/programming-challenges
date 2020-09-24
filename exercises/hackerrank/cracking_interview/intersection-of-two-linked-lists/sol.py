# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1 = headA
        p1List = "first"
        p2 = headB
        p2List = "sec"
        rounds = 0
        while p1 != p2:
            if p1.next is None:
                rounds += 1
                if rounds > 1:
                    return None
                if p1List == "first":
                    p1 = headB
                    p1List = "sec"
                else:
                    p1 = headA
                    p1List = "first"
            else:
                p1 = p1.next
            if p2.next is None:
                if p2List == "sec":
                    p2 = headA
                    p2List = "first"
                else:
                    p2 = headB
                    p2List = "sec"
            else:
                p2 = p2.next

        return p1
        
        