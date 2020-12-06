# 1681. Minimum Incompatibility
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        '''
        State compression DFS.
        The key is to change the caching state, from all possible subsets,
        to available elements from nums. This reduces state space from
        k(n^(n/k)) (up to 2 * 16^8 when n = 16, k = 2) to n(2^n) (up to
        16 * 2^16, aka, 2^20).
        The DFS recursion returns the min score from arr split into subsets
        of target_size, one subset at a time. Leverage built-in combinations()
        to get candidate subsets.

        Time: O(n 2^n) where n is len(nums)
        Space: O(2^n)
        '''
        n = len(nums)
        target_size = n // k

        @lru_cache(None)
        def dfs(arr):
            if not arr:
                return 0
            ans = inf
            for a in combinations(set(arr), target_size):
                others = list(arr)
                for v in a:
                    others.remove(v)
                ans = min(ans, max(a) - min(a) + dfs(tuple(others)))
            return ans

        ans = dfs(tuple(nums))
        return ans if ans != inf else -1