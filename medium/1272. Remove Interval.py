# 1272. Remove Interval
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        '''
        Array.
        Only worry about the intersections. The key is to be concise.

        Time: O(n) where n is the size of the intervals array.
        Space: O(n)
        '''
        low, high = toBeRemoved
        ans = []
        for s, e in intervals:
            if low > s:
                ans.append([s, min(low, e)])
            if e > high:
                ans.append([max(high, s), e])
        return ans