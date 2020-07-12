import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or head.next == None:
            return head
        mappings = []
        item = head
        while item:
            mappings.append(item)
            item = item.next

        total = len(mappings)
        upTo = math.floor(total/2)
        for i in range(upTo):
            mappings[i].next = mappings[total-1-i]
            mappings[total-1-i].next = mappings[i+1]
        
        mappings[i+1].next = None

        return mappings[0]
