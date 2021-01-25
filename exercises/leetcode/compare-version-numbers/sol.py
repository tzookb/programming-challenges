import itertools

class Solution:
    def getVersionNumbers(self, version: str) -> List[int]:
        split_versions = version.split(".")
        nums = [0] * len(split_versions)
        for idx, v in enumerate(split_versions):
            
            nums[idx] = int(v)
        return nums
        
    def compareVersion(self, version1: str, version2: str) -> int:
        one = self.getVersionNumbers(version1)
        two = self.getVersionNumbers(version2)

        for a, b in itertools.zip_longest(one, two):
            a = 0 if a is None else a
            b = 0 if b is None else b

            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
        