class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        Typical DFS. Just pay attention to the *index* that you pass into
        recursive calls!
        '''
        ans = 0
        def dfs(start, curr):
            nonlocal ans
            isUnique = len(curr) == len(set(curr))
            if isUnique:
                ans = max(ans, len(curr))
            if start == len(arr) or not isUnique:
                return
            
            for i in range(start, len(arr)):
                dfs(i + 1, curr + arr[i])
        dfs(0, "")
        return ans