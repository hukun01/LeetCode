# 1539. Kth Missing Positive Number
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        Binary search.
        Notice that arr is sorted in increasing order and starts from 1, so
        the missing count in the first arr[:m+1] would be arr[m] - (m + 1).
        The missing count monotonically goes up when m increases, so we can
        do binary search.
        The range of m is [0, len(arr)], if the missing count is less than k,
        we know the k-th missing number is on the right, otherwise it's on
        the left.
        After the above search, we know that in the first l numbers the
        missing count is k, so the answer is l + k, because we want to skip
        k numbers that are missing in the first l numbers in arr.
        '''
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k