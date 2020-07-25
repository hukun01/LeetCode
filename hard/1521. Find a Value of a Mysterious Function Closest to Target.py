# 1521. Find a Value of a Mysterious Function Closest to Target
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        '''
        Bit manipulation and DP.
        
        A key is to notice that as we expend the interval, the
        func result is non-increasing.

        Let AND(i, j) denote arr[i] & arr[i+1] & ... & arr[j].
        For a fixed j, let s(j) record all the results of AND(i, j) where 0 <= i <= j.
        Then s(j + 1) = {arr[j + 1]} | {arr[j + 1] & a} for all a in s(j).
        Therefore we can get all s(0), s(1), ..., s(n-1) and find the answer.
        The size of each s(j) is O(logm) where m = max(arr).
        '''
        s = set()
        ans = math.inf
        for a in arr:
            s = {a & b for b in s} | {a}
            ans = min(ans, min(abs(c - target) for c in s))
        return ans