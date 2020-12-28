class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        Greedy
        This is the same as Interval Scheduling problem.
        Use greedy after sort by ending time.

        Time: O(n log(n)) where n is len(pairs)
        Space: O(n)
        '''
        ans = 0
        cur_end = -inf
        for start, end in sorted(pairs, key=lambda p:p[1]):
            if cur_end < start:
                cur_end = end
                ans += 1
        return ans