# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Notice those keywords: sorted, median
        Think about binary search.

        Divide all elements in {A, B} into two parts, ensure that both are equal length, 
        and left part is always smaller than right part. 
        Then median = (max(left_part) + min(right_part))/2.

        Let 'a' be the length of A's left partition, 'b' be the length of B's left partition.
        Our goal is to find out the proper 'a' and 'b' such that
        1. a + b == m + n - (a + b)
           both (m + n) and (m + n + 1) works,
           we use (m + n + 1) so we return leftMax if the (m + n) is odd;
        
        2. max(A[a-1], B[b-1]) <= min(A[a], B[b])

        Because we can derive 'b' from 'a' given the above conditions, we just
        need to find out the proper 'a'. 

        https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)
        # Ensure m <= n, so the 'b' below will not exceed the B's index range.
        # A simple example can prove why this is necessary: A=[1,3], B=[2]
        if m > n:
            A, B, m, n = B, A, n, m
        
        halfLen = (m + n + 1) // 2
        
        l, h = 0, m
        while l <= h:
            a = (l + h) // 2
            b = halfLen - a
            # A[a-1] is too big, we decrease 'a' to make A[a-1] <= B[b]
            if a > 0 and A[a - 1] > B[b]:
                h = a - 1
            # B[b-1] is too big, we decrease 'b' by increasing 'a', to make B[b-1] <= A[a]
            elif a < m and B[b - 1] > A[a]:
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
                    rightMin = A[a]
                else:
                    rightMin = min(A[a], B[b])
                    
                return (leftMax + rightMin) / 2
