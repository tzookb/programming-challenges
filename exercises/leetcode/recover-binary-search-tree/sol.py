class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arr_to_tree(items: List[int]) -> Optional[TreeNode]:
    if not items:
        return None
    
    root = TreeNode(items.pop(0))
    queue = [root]

    while items:
        cur = queue.pop(0)

        if items:
            left = items.pop(0)
            if left:
                cur.left = TreeNode(left)
                queue.append(cur.left)

        if items:
            right = items.pop(0)
            if right:
                cur.right = TreeNode(right)
                queue.append(cur.right)

    return root

def getInOrder(root: Optional[TreeNode]) -> List[int]:
    inorder = []
    stack = [(root, False)]

    while stack:
        cur, processed = stack.pop()
        if not cur:
            continue
        if processed:
            inorder.append(cur.val)
            continue
        
        stack.append((cur.right, False))
        stack.append((cur, True))
        stack.append((cur.left, False))
    
    return inorder

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        inorder = getInOrder(root)
        inorder.sort()
        
        stack = [(root, False)]
        while stack:
            cur, processed = stack.pop()
            if not cur:
                continue
            if processed:
                if inorder[0] != cur.val:
                    cur.val = inorder[0]
                inorder.pop(0)
                continue
            
            stack.append((cur.right, False))
            stack.append((cur, True))
            stack.append((cur.left, False))
