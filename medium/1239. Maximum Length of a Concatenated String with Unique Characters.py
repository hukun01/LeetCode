class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        Typical DFS. Just pay attention to the *index* that you pass into
        recursive calls!
        '''
        arr = [a for a in arr if len(set(a)) == len(a)]
        self.ans = 0
        def dfs(idx, curr):
            self.ans = max(self.ans, len(curr))
            for i in range(idx, len(arr)):
                chars = set(arr[i])
                if len(curr & chars) == 0:
                    dfs(i + 1, curr | chars)
        dfs(0, set())
        return self.ans
        '''
        Another style of DFS.
        '''
        self.ans = 0
        def dfs(start, curr):
            isUnique = len(curr) == len(set(curr))
            if isUnique:
                self.ans = max(self.ans, len(curr))
            else:
                return
            
            for i in range(start, len(arr)):
                dfs(i + 1, curr + arr[i])
        dfs(0, "")
        return self.ans