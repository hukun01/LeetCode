class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        DFS with backtrack. No sorting needed.
        Similar to 1079 Letter Tile Possibilities, use a counter to avoid duplicate usage.
        '''
        counter = collections.Counter(nums)
        ans = []
        def dfs(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for n in counter:
                if counter[n] <= 0:
                    continue
                curr.append(n)
                counter[n] -= 1
                dfs(curr)
                curr.pop()
                counter[n] += 1
        dfs([])
        return ans