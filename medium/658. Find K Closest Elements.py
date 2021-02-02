# 658. Find K Closest Elements
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        Binary-search for where the resulting elements start in the array.
        It's the first index i so that arr[i] is better than arr[i+k] 
        (with "better" meaning closer to or equally close to x). 
        Then just return the k elements starting there.

        Note that we can't use abs() for diffs or it will fail in below case:
        [1,1,2,2,2,3,3], k = 2, x = 3
        The order of x and arr[m] in the diff calculation should be clear if
        we list out all possible cases:
        1. x, arr[mid], arr[mid + k]
        2. arr[mid], arr[mid + k], x
        3. arr[mid], x, arr[mid + k]

        The #1 and #2 cases are straightforward. We need to move left in #1,
        and move right in #2. The tricky part is #3. We use the relative
        distance between (arr[m], x) and (x, arr[m + k]) to measure which
        direction we should go.
        If arr[m] - x + arr[m + k] - x >= 0, means arr[m + k] is relatively
        large (but may be just good), we should cap h = m; Otherwise, arr[m]
        is so small that we have to exclude it in the next round, by l = m + 1.

        Now apply #3 logic in #1 and #2, and turns out the #3 logic universally
        applies to #1 and #2.
        '''
        l = 0
        h = len(arr) - k
        while l < h:
            m = (l + h) // 2
            if arr[m] - x + arr[m + k] - x >= 0:
                h = m
            else:
                l = m + 1
        return arr[l: l + k]