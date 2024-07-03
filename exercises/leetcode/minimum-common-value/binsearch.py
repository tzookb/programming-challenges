class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binSearch(target: int, items):
            left = 0
            right = len(items) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if items[mid] == target:
                    return True
                elif items[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return False

        
        if len(nums1) > len(nums2):
            longer = nums1
            shorter = nums2
        else:
            longer = nums2
            shorter = nums1

        for target in shorter:
            if binSearch(target, longer):
                return target
            
        return -1
        