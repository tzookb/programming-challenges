from heapq import heappop, heappush
from typing import Counter



class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        items = []
        cnt = Counter(list(s))
        for c in cnt:
            heappush(items, (-cnt[c], c))
        
        last_pos = {}
        arranged = [None]
        left = [None] * (k - 1)
        while items:
            print(left, items, arranged)
            print("---")
            times, highest = heappop(items)
            times = -times
            if arranged[-1] == highest:
                return ""
            
            cur_pos = len(arranged)
            if highest in last_pos and last_pos[highest] + k > cur_pos:
                return ""
            last_pos[highest] = cur_pos
            arranged.append(highest)

            return_item = left.pop()

            if return_item:
                heappush(items, return_item)
            
            if times > 1:
                left.insert(0, (-(times - 1), highest))
            else:
                left.insert(0, None)

        while left:
            return_item = left.pop()
            if not return_item:
                continue
            val = return_item[1]
            if -return_item[0] > 1:
                return ""
            if val == arranged[-1]:
                return ""
            cur_pos = len(arranged)
            if val in last_pos and last_pos[val] + k > cur_pos:
                return ""

            last_pos[val] = cur_pos
            arranged.append(val)
        
        arranged.pop(0)
        return "".join(arranged)

s = Solution()
# res = s.rearrangeString("aabbcc", 3) # abcabc
# res = s.rearrangeString("aaabc", 3) # ""
# res = s.rearrangeString("aaabc", 2) # "abaca"
res = s.rearrangeString("aaadbbcc", 2) # "abcabcad"
# res = s.rearrangeString("abb", 3) # ""
print(res)