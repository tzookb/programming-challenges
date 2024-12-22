from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def recu(start: Optional[ListNode]):
            if not start:
                return None
            
            mid = self.get_linked_list_mid(start)
            left, mid, right = self.break_linked_list_node(start, mid)
            
            lefttree = recu(left)
            righttree = recu(right)
            return TreeNode(mid.val, lefttree, righttree)

        return recu(head)
    
    def break_linked_list_node(self, head: Optional[ListNode], breakpoint: Optional[ListNode]):
        if not head:
            return [None, None, None]
        if not head.next:
            return [head, breakpoint, None]
        left = head
        while left.next != breakpoint:
            left = left.next
        left.next = None

        right = breakpoint.next
        breakpoint.next = None

        return [left, breakpoint, right]

    def get_linked_list_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# s = Solution()
# s.sortedListToBST()