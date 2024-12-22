# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        cur = []
        curlevel = 0
        bst = [(root, 0)]

        while bst:
            item, level = bst.pop(0)
            if not item:
                continue
            if level != curlevel:
                sumed = sum(cur)
                if len(heap) < k:
                    heappush(heap, sumed)
                elif heap[0] < sumed:
                    heappop(heap)
                    heappush(heap, sumed)
                cur = []
                curlevel = level
            
            cur.append(item.val)

            bst.append((item.left, curlevel + 1))
            bst.append((item.right, curlevel + 1))
        
        sumed = sum(cur)
        if len(heap) < k:
            heappush(heap, sumed)
        elif heap[0] < sumed:
            heappop(heap)
            heappush(heap, sumed)
        
        print(heap)
        if len(heap) < k:
            return -1

        return heap[0]
        