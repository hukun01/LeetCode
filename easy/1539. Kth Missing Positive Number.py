# 1539. Kth Missing Positive Number
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        Binary search.
        Notice that arr is sorted in increasing order and starts from 1, so
        the missing count in the first arr[:m+1] is arr[m] - (m + 1).
        The missing count monotonically goes non-decreasing when m increases,
        so we can do binary search.
        The range of l is [0, len(arr)], if the missing count is less than k,
        we know the k-th missing number is on the right, otherwise it's on
        the left.
        We look for the smallest l such that missing count in arr[:l+1] >= k.

        After the search, in arr[:l] the missing count X = arr[l-1] - l < k.
        We need to add (k - X) more missing numbers, and we know those numbers
        are between arr[l-1] and arr[l], because arr[l] - (l + 1) >= k.
        The answer is arr[l-1] + (k - X) = arr[l-1] + k - arr[l-1] + l = l + k.

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