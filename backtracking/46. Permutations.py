# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtrack DFS, we check whether an element has been visited, if yes, skip;
        if not, continue to DFS with an expanded current list
        '''
        ans = []
        def dfs(used, comb):
            if len(comb) == len(nums):
                ans.append(comb[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                comb.append(nums[i])
                used.add(i)
                dfs(used, comb)
                comb.pop()
                used.remove(i)
        dfs(set(), [])
        return ans