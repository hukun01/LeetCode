# 1775. Equal Sum Arrays With Minimum Number of Operations
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 < s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
            
        if n1 * 6 < n2 or n2 * 6 < n1:
            return -1

        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = 0
        total_diff = s1 - s2 # s1 >= s2
        for i in range(6):
            count = c1[6 - i] + c2[1 + i]
            delta = 5 - i
            gap = delta * count
            if gap < total_diff:
                total_diff -= gap
                res += count
            elif gap >= total_diff:
                count = ceil(total_diff / delta)
                total_diff -= gap
                res += count
            if total_diff <= 0:
                return res