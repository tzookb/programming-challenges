class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # the smallest (first) and the largest (last) nodes
        first, last = None, None

        def helper(node):
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)
        
        if not root:
            return None
        
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first