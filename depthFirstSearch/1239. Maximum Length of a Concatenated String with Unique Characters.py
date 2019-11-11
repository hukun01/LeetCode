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
            else:
                return
            
            for i in range(start, len(arr)):
                dfs(i + 1, curr + arr[i])
        dfs(0, "")
        return ans
        '''
        Another style with set operations.

        arr = [a for a in arr if len(set(a)) == len(a)]
        ans = 0
        def dfs(idx, curr):
            nonlocal ans
            ans = max(ans, len(curr))
            for i in range(idx, len(arr)):
                chars = set(arr[i])
                if len(curr & chars) == 0:
                    dfs(i + 1, curr | chars)
        dfs(0, set())
        return ans
        '''