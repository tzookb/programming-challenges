# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = []
        if self.root:
            self.nodes.append(self.root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.nodes:
            node = self.nodes.pop(0)
            if node.right:
                self.nodes.insert(0, node.right)
                node.right = None
            if node.left:
                self.nodes.insert(0, node)
                self.nodes.insert(0, node.left)
                node.left = None
            else:
                return node.val
        return -1
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.nodes)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()