from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        helper_head = ListNode(0, head)
        adapted_k = k + 1
        list_size = self.getListSize(helper_head)
        left_prev, left_node = self.getKthNodeAndPrev(helper_head, adapted_k)
        k_from_right = list_size - adapted_k + 2
        right_prev, right_node = self.getKthNodeAndPrev(helper_head, k_from_right)

        left_prev.next = right_node
        right_prev.next = left_node
        
        left_next = left_node.next
        left_node.next = right_node.next
        right_node.next = left_next

        return helper_head.next
        

    def getKthNodeAndPrev(self, head: Optional[ListNode], k: int):
        count = 0
        cur = head
        prev = None
        while cur:
            count += 1
            if count == k:
                return (prev, cur)
            prev = cur
            cur = cur.next
        
        raise "k is to far for list"

    def getListSize(self, head: Optional[ListNode]) -> int:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        return count