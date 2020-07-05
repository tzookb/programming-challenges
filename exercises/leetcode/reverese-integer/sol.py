class Solution:
    def reverse(self, x: int) -> int:
      if x == 0:
        return 0
      not_bigger_then = 2**31

      left = abs(x)
      sign = x / abs(x)
      sum = 0
      while True:
        remainder = left % 10
        left = (left - remainder)/10
        sum = sum * 10 + remainder
        if left == 0:
          break
      if not_bigger_then < sum:
        return 0
      return int(sign * sum)


s = Solution()
res = s.reverse(120)
print(res)