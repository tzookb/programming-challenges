# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDeleteMap = {}
        for delItem in to_delete:
            toDeleteMap[delItem] = True

        def recu(node: Optional[TreeNode]):
            if not node:
                return (None, [])
            
            leftnode, lefttrees = recu(node.left)
            rightnode, righttrees = recu(node.right)

            if node.val in toDeleteMap:
                #should skip this node:
                subtrees = lefttrees + righttrees
                if leftnode:
                    subtrees.append(leftnode)
                if rightnode:
                    subtrees.append(rightnode)
                return (
                    None,
                    subtrees
                )
            else:
                node.left = leftnode
                node.right = rightnode

                return (
                    node,
                    lefttrees + righttrees
                )


        
        cur, trees = recu(root)

        if cur:
            return [cur] + trees
        
        return trees
        