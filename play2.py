from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        graph = self.buildGrap(root)
        visited = {}
        cnt = 0

        bfs = [(target.val, 0)]
        while bfs:
            cur, dist = bfs.pop()
            if not cur:
                continue
            if cur in visited:
                continue
            visited[cur] = True
            if dist == k:
                result.append(cur)
                continue

            children = graph[cur]
            for child in children:
                bfs.append((child, dist + 1))
        
        return result



    def buildGrap(self, root: TreeNode) -> List[int]:
        paths = {}
        paths[root.val] = {}
        bfs = [root]
        while bfs:
            cur = bfs.pop()
            if cur.left:
                paths[cur.val][cur.left.val] = True
                if cur.left.val not in paths:
                    paths[cur.left.val] = {}
                paths[cur.left.val][cur.val] = True
                bfs.append(cur.left)
            if cur.right:
                paths[cur.val][cur.right.val] = True
                if cur.right.val not in paths:
                    paths[cur.right.val] = {}
                paths[cur.right.val][cur.val] = True
                bfs.append(cur.right)
        return paths

# s = Solution()
# res = s.distanceK()
# print(res)