# 131. Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        DFS with backtrack.
        For the current i, if s[:i] is a palindrome, add it to path and try
        dfs on s[i:], then come back and try the next i.

        Time: O(n 2^n) where n is len(s). There's (n-1) options to cut s or
              skip it, so there's 2^n total choices. For every cut, we need
              O(n) time to check whether every substring is palindrome. Of
              course we also need O(n) time to replicate it, but that happens
              along with palindrome test.
        Space: O(n^2) to store output.
        '''
        def dfs(s, path, ans):
            if not s:
                ans.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, ans)
                    path.pop()        
        ans = []
        dfs(s, [], ans)
        return ans