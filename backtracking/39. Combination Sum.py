class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        DFS with backtracking.
        '''
        ans = []
        def dfs(nums, idx, remaining):
            if remaining < 0:
                return
            if remaining == 0:
                ans.append(nums[:])
                return
            
            for i in range(idx, len(candidates)):
                curr = candidates[i]
                nums.append(curr)
                dfs(nums, i, remaining - curr)
                nums.pop()
        
        dfs([], 0, target)
        return ans