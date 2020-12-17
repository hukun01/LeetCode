# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtrack DFS
        Wheck whether an element has been visited, if yes, skip; if not,
        continue to DFS with an expanded current list.

        Time: O(n!) where n is len(nums)
        Space: O(n(n!))
        '''
        ans = []
        n = len(nums)
        def dfs(used, curr):
            if len(curr) == n:
                ans.append(curr[:])
                return
            for i in range(n):
                if i in used:
                    continue
                curr.append(nums[i])
                used.add(i)
                dfs(used, curr)
                curr.pop()
                used.remove(i)
        dfs(set(), [])
        return ans