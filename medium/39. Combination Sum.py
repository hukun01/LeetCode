# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        DFS with backtracking.
        '''
        ans = []
        def dfs(idx, currList, currSum):
            if currSum >= target:
                if currSum == target:
                    ans.append(currList[:])
                return
            for i in range(idx, len(candidates)):
                currList.append(candidates[i])
                dfs(i, currList, currSum + candidates[i])
                currList.pop()
        dfs(0, [], 0)
        return ans