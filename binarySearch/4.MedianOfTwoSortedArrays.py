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
        A, B = nums1, nums2
        m, n = len(A), len(B)
        # m must be smaller or equal to n, so later b can be non-negative.
        if m > n:
            A, B, m, n = B, A, n, m
        halfLen = (m + n + 1) // 2
        
        # Pay close attention to the below 2 lines: 
        # the search space for i must be [0, m], 
        # and l <= h to make sure we never break the while loop!
        l, h = 0, m
        while l <= h:
            a = l + (h - l) // 2
            b = halfLen - a
            if a > 0 and A[a - 1] > B[b]:
                h = a - 1
            elif a < m and B[b - 1] > A[a]:
                # B[b - 1] is too big, to decrease b, we can increase a
                l = a + 1
            else:
                # a is good, 
                # find out the max in the left part
                if a == 0:
                    leftMax = B[b - 1]
                elif b == 0:
                    leftMax = A[a - 1]
                else:
                    leftMax = max(A[a - 1], B[b - 1])
                    
                if (m + n) % 2 == 1:
                    return leftMax
                
                # find out the min in the right part
                if a == m:
                    rightMin = B[b]
                elif b == n:
                    rightMin = A[0]
                else:
                    rightMin = min(A[a], B[b])
                    
                return (leftMax + rightMin) / 2