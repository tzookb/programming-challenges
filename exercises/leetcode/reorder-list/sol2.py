from distutils.command.build import build
import time
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        middle_list = self.getMiddleNode(head)
        middle_list = self.reverseList(middle_list)

        merged = self.mergeLists(head, middle_list)
        return merged


    def mergeLists(self, first: ListNode, second: ListNode) -> ListNode:
        cur_pos = ListNode()
        left = first
        right = second
        while left or right:
            # print(getArrFromList(left), getArrFromList(right))
            if left:
                cur_pos.next = left
                cur_pos = cur_pos.next
                left = left.next

            if right:
                cur_pos.next = right
                cur_pos = cur_pos.next
                right = right.next
                

        return first

    def getMiddleNode(self, head: ListNode) -> ListNode:
        prev_slow = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next
        
        to_ret = slow.next
        slow.next = None
        return to_ret

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            next_cur = cur.next
            cur.next = prev
            prev = cur
            cur = next_cur
        
        return prev



def buildList(arr):
    fake_head = ListNode()
    prev = fake_head
    for item in arr:
        next_val = ListNode(item)
        prev.next = next_val
        prev = next_val
    return fake_head.next

def getArrFromList(head):
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr

head = buildList([1,2,3,4,5,6])
s = Solution()
res = s.reorderList(head)
# res = s.getMiddleNode(head)
# res = s.reverseList(head)
