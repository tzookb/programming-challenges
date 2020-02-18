# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        listHead = ListNode(None)
        res = listHead
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            cur1Val = cur1.val
            cur2Val = cur2.val
            if cur1Val > cur2Val:
                curItem = cur2
                cur2 = cur2.next
            else:
                curItem = cur1
                cur1 = cur1.next
            nextRes = ListNode(curItem.val)
            res.next = nextRes
            res = nextRes
        
        if cur1:
            res.next = cur1

        if cur2:
            res.next = cur2
        
        return listHead.next
