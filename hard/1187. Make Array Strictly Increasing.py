# 1187. Make Array Strictly Increasing
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        DP. Similar to the DP solution of 300. Longest Increasing Subsequence.
        Use a dict to record the mapping of {element: ops}.
        For each element in arr1, we know the last possible elements and ops.
        For every possible last element, if the current element is greater than
        it, we save it and the ops in a current dict; otherwise, we need to find
        in arr2 the smallest element that's greater than the last element, and ops + 1.
        '''
        dp = {-1:0}
        arr2.sort()
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i],dp[key])
                loc = bisect_right(arr2,key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]],dp[key]+1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1