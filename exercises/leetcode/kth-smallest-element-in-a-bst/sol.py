class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        cur_count = 0

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                cur_count += 1
                if cur_count == k:
                    return current.val
                current = current.right
            else:
                break
        return self.ans