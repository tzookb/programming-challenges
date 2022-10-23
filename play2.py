from heapq import heapify, heappop, heappush
from typing import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        items = list(zip([-ord(k) for k in cnt.keys()], cnt.values()))
        heapify(items)
        final = [None]

        while items:
            neg_asc_code, count = heappop(items)
            c = chr(-neg_asc_code)

            if c == final[-1]:
                if not items:
                    break

                sec_neg_asc_code, sec_count = heappop(items)
                sec_c = chr(-sec_neg_asc_code)
                final.append(sec_c)

                heappush(items, (-ord(c), count))
                if sec_count > 1:
                    heappush(items, (-ord(sec_c), sec_count - 1))
            else:
                add_size = min(repeatLimit, count)
                final += [c] * add_size
                if count - add_size > 0:
                    heappush(items, (-ord(c), count - add_size))

        return "".join(final[1:])


        

s = Solution()
res = s.repeatLimitedString("cczazcc", 3)
# res = s.repeatLimitedString("aababab", 2)
print(res)