class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Notice those keywords: sorted, median
        Think about binary search.

        Divide all elements in {A, B} into two parts, ensure that both are equal length, 
        and left part is always smaller than right part. 
        Then median = (max(left_part) + min(right_part))/2.
        https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        # m must be smaller or equal to n, so j can be non-negative.
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        # Pay close attention to the below 2 lines: 
        # the search space for i must be [0, m], 
        # and l <= h to make sure we never break the while loop!
        l, h, halfLen = 0, m, (m + n + 1) // 2
        while l <= h:
            i = (l + h) // 2
            j = halfLen - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                # nums1[i - 1] is too big, decrease i
                h = i - 1
            # when j > 0, i could be m, so we must check i < m
            elif i < m and nums2[j - 1] > nums1[i]:
                # nums2[j - 1] is too big, decrease j => increase i
                l = i + 1
            else:
                # i is good, 
                # find out the max in the left part
                if i == 0:
                    leftMax = nums2[j - 1]
                elif j == 0:
                    leftMax = nums1[i - 1]
                else:
                    leftMax = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2 == 1:
                    return leftMax
                
                # find out the min in the right part
                if i == m:
                    rightMin = nums2[j]
                elif j == n:
                    rightMin = nums1[i]
                else:
                    rightMin = min(nums2[j], nums1[i])
                    
                return (leftMax + rightMin) / 2