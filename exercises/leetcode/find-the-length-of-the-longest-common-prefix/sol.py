class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes1 = {}
        matches = 0
        for t1 in arr1:
            st1 = str(t1)
            for i in range(len(st1)):
                prefix = st1[0:i+1]
                prefixes1[prefix] = True

        longest = 0
        for t2 in arr2:
            st2 = str(t2)

            for i in range(len(st2)):
                prefix = st2[0:i + 1]

                if prefix in prefixes1:
                    longest = max(longest, len(prefix))

        return longest