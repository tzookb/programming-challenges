from typing import List, Counter

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        x = list('{0:b}'.format(n))
        size = len(x)
        diff = 32 - size
        if diff:
            extra = ["0"] * diff
            x = extra + x
            
        x = x[::-1]
        x = "".join(x)
        
        x = int(x, 2)

        return x
        
s = Solution()
s.reverseBits(8)
