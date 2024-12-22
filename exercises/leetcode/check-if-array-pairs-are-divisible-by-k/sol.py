class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) % k != 0:
            return False

        minis = [n % k for n in arr]
        
        mapped = Counter()
        for num in minis:
            partner = k - num
            if partner in mapped:
                mapped[partner] -= 1
                if mapped[partner] == 0:
                    del mapped[partner]
            else:
                mapped[num] += 1
        
        if mapped[0]:
            if mapped[0] % 2 == 0:
                del mapped[0]
            else:
                return False
        
        
        return not mapped
        