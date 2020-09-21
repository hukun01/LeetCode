# 370. Range Addition
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        '''
        Array.
        The technique is to have a rolling update array that first collects
        the start and end positions for each udpate interval, and record the
        delta, by adding `delta` to start, and minus `delta` to (end+1).
        Later we compute prefix sum for this array, and the `delta` in start
        will be accumulated to every position after it, until (end+1), after
        which the accumulated `delta` will be negated.
        '''
        ans = [0] * length
        for s, e, d in updates:
            ans[s] += d
            if e + 1 < length:
                ans[e + 1] -= d
        for i in range(1, length):
            ans[i] += ans[i-1]
        return ans