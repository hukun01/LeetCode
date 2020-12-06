# 1539. Kth Missing Positive Number
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        Binary search.
        Notice that arr is sorted in increasing order and starts from 1, so
        the missing count in the first arr[:m+1] is arr[m] - (m + 1).
        The missing count monotonically goes non-decreasing when m increases,
        so we can do binary search.
        The range of m is [0, len(arr)], if the missing count is less than k,
        we know the k-th missing number is on the right, otherwise it's on
        the left.
        After the above search, we know that either:
        1. l == 0, in [1:arr[l]] the missing count is at least k, so the
           answer is just k.
        2. l > 0, in arr[:l], the missing count is X = arr[l-1] - (l-1+1) < k.
           So the answer is arr[l-1] + k - X = l + k.
        We can merge both cases to be l + k.

        The key is to identify that the missing count in the first arr[:m+1]
        is arr[m] - (m + 1).

        Time: O(log(n)) where n is len(arr)
        Space: O(1)
        '''
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k