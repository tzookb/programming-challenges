class Solution:

    def recu(self, node: TreeNode, p: TreeNode, q: TreeNode) -> (TreeNode, object):
        founds = {"p": False, "q": False}
        if node is None:
            return (None, founds)

        foundsLeft = self.recu(node.left, p, q)
        foundsRight = self.recu(node.right, p, q)

        founds["p"] = (
            node.val == p.val or
            foundsLeft[1]["p"] or
            foundsRight[1]["p"]
        )
        founds["q"] = (
            node.val == q.val or
            foundsLeft[1]["q"] or
            foundsRight[1]["q"]
        )
        if founds["p"] and founds["q"]:
            foundNode = foundsLeft[0] if foundsLeft[0] else foundsRight[0]
            if foundNode:
                return (foundNode, founds)
            else:
                return (node, founds)
        return (None, founds)

    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = self.recu(node, p, q)
        return result[0]
