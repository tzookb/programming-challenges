# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fakeHead = ListNode()
        fakeHead.next = head
        count = 0
        node = fakeHead
        while node:
            count += 1
            node = node.next
        
        node = fakeHead
        stop = count - n
        count = 0
        while node:
            count += 1
            if stop == count:
                node.next = node.next.next
                break
            node = node.next
        return fakeHead.next

