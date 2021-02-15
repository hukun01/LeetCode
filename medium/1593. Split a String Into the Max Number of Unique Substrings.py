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
        n = len(s)
        self.ans = 0
        def dfs(i, used):
            if i == n:
                self.ans = max(self.ans, len(used))
                return

            for j in range(i, n):
                part = s[i:j + 1]
                if part in used:
                    continue
                if n - i + len(used) <= self.ans:
                    continue
                used.add(part)
                dfs(j + 1, used)
                used.remove(part)

        dfs(0, set())
        return self.ans