class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtrack DFS, we check whether an element has been visited, if yes, skip;
        if not, continue to DFS with an expanded current list
        '''
        ans = []
        def dfs(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for c in nums:
                if c in curr:
                    continue
                curr.append(c)
                dfs(curr)
                curr.pop()
        dfs([])
            
        return ans