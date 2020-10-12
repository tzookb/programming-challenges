class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        half = l // 2
        for i in range(half):
            end = l - 1 - i
            s[i], s[end] = s[end], s[i]
        