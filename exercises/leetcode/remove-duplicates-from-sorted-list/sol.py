# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        item = head

        while item and item.next:
            if item.val == item.next.val:
                item.next = item.next.next
            else:
                item = item.next
            
        return head