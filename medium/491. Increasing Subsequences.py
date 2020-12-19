# 491. Increasing Subsequences
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        DFS backtrack.
        The key is to de-dup nicely. Naive way is to use a set for everything.
        The trick is to have a used set to track the used values in *current*
        recursion, this way we can avoid having duplicate [1,1] from [1,2,1,1],
        because only each '1' will be used only once in each recursion.

        This is also the reason why the problem states "two equal integers
        should also be considered as a special case of increasing sequence".

        Time: O(2^n) where n is len(nums), worse case when nums is sorted.
        Space: O(n (2^n))
        '''
        n = len(nums)
        ans = []
        def dfs(i, cur):
            if len(cur) >= 2:
                ans.append(cur[:])
            used = set()
            for j in range(i, n):
                if nums[j] in used:
                    continue
                if cur and nums[j] < cur[-1]:
                    continue
                used.add(nums[j])
                cur.append(nums[j])
                dfs(j+1, cur)
                cur.pop()
        dfs(0, [])
        return ans