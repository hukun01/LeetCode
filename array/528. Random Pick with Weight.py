class Solution:
    '''
    Accumulate the weights, and pick a random weight from [0, total),
    and use binary search to find its interval index in the accumulated array.

    Note that in the binary search, if target == arr[m], we can't keep m,
    but we need to make l = m + 1. Consider the accumulated array being [3, 10],
    the intervals would be [[0, 3), [3, 10)], if target is 3, we need to go to the
    next interval.
    '''
    def __init__(self, w: List[int]):
        self.runningSums = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        w = random.randrange(self.runningSums[-1])
        return self.findLowerBound(self.runningSums, w)
    
    def findLowerBound(self, arr, target):
        l, h = 0, len(arr) - 1
        while l < h:
            m = (l + h) // 2
            if arr[m] <= target:
                l = m + 1
            else:
                h = m
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()