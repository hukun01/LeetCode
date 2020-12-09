# 1593. Split a String Into the Max Number of Unique Substrings
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        '''
        DFS with backtrack and pruning.
        Backtrack: iterate through all possible cutting positions, and try each
        part and come back.
        Pruning: only try above when the best case (where each char is an unique
        substring) can beat the current answer.

        Note that in backtracking problems we usually can't do memoization.

        Time: O(n^k) from n!/(n-k)!, where n is len(s), k is the max answer.
        Space: O(n)
        '''
        def dfs(s, curr_set):
            if not s:
                return 0
            ans = 0
            n = len(s)
            for i in range(1, n + 1):
                if (part := s[:i]) not in curr_set and n - i + 1 > ans:
                    curr_set.add(part)
                    ans = max(ans, 1 + dfs(s[i:], curr_set))
                    curr_set.remove(part)
            return ans
        return dfs(s, set())