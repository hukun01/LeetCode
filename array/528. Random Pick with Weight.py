class Solution:
    '''
    TODO
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