class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        '''
        Sort the array and shrink from two ends.
        The reason why we can do this is that, when sum is greater than K,
        we only want to make the sum smaller by reducing the right; when sum
        is less than K, we record the current answer, and explore the possibly
        bigger sum by increasing the left.
        In each iteration, we make some progress on shrinking the array.
        '''
        A.sort()
        left, right = 0, len(A)-1
        ans = -1
        while left < right:
            if A[left] + A[right] < K:
                ans = max(ans, A[left] + A[right])
                left += 1
            else:
                right -= 1
        return ans