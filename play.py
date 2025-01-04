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
            left = start
            right = mid.next
            mid.next = None
            
            lefttree = recu(left)
            righttree = recu(right)
            return TreeNode(mid.val, lefttree, righttree)

        return recu(head)

    def get_linked_list_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        return slow

# s = Solution()
# s.sortedListToBST()