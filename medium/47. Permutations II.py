# 47. Permutations II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        DFS with backtrack. No sorting needed.

        Similar to 1079 Letter Tile Possibilities, use a counter to avoid
        duplicate usage.
        '''
        counter = Counter(nums)
        ans = []
        def dfs(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for n in counter:
                if counter[n] == 0:
                    continue
                curr.append(n)
                counter[n] -= 1
                dfs(curr)
                curr.pop()
                counter[n] += 1

        dfs([])
        return ans
        '''
        2/2 Generator version of 1/2.
        '''
        counter = Counter(nums)
        def dfs(curr):
            if len(curr) == len(nums):
                yield curr[:]
            for n in counter:
                if counter[n] == 0:
                    continue
                curr.append(n)
                counter[n] -= 1
                yield from dfs(curr)
                curr.pop()
                counter[n] += 1

        return [x for x in dfs([])]