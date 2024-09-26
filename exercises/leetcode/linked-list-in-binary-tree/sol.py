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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        bfs = [root]
        while bfs:
            cur = bfs.pop(0)
            if not cur:
                continue
            print(cur.val)
            if self.comparePathFromPlace(head, cur):
                return True
            bfs.append(cur.left)
            bfs.append(cur.right)
        return False

    def comparePathFromPlace(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head and not root:
            return True
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        
        if self.comparePathFromPlace(head.next, root.left):
            return True

        return self.comparePathFromPlace(head.next, root.right)

        