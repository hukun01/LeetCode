# 1775. Equal Sum Arrays With Minimum Number of Operations
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Greedy.
        Let nums1 be the array with larger sum.
        We want to reduce total_diff to 0, with the min number of steps.
        The quickest way is to decrease 6 to 1 in nums1, and to increase 1 to
        6 in nums2. Then to decrease 5 to 1 in nums1, and to increase 2 to 6
        in nums2. 
        The change goes from big to small, from 5 to 1, inclusive.
        For each change, we pick the largest values in nums1 and decrease them
        to 1, and we pick the smallest values in nums2 and increase them to 6.

        Time: O(n)
        Space: O(n)
        '''
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 * 6 < n2 or n2 * 6 < n1:
            return -1

        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 < s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1

        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = 0
        total_diff = s1 - s2 # s1 >= s2
        for change in range(5, 0, -1):
            count = c1[change + 1] + c2[6 - change]
            diff = change * count
            if diff < total_diff:
                ans += count
                total_diff -= diff
            else:
                ans += ceil(total_diff / change)
                total_diff -= diff
                break

        return ans