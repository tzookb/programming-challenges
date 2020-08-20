class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        dist = float('inf')
        distVal = None
        node = root
        while node:
            curDist = node.val - target
            if abs(curDist) < dist:
                dist = abs(curDist)
                distVal = node.val
            if curDist > 0:
                node = node.left
            else:
                node = node.right
        return distVal