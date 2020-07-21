# 403. Frog Jump
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        DFS with memoization.
        '''
        if stones[1] != 1:
            return False
        @lru_cache(None)
        def dfs(stone_idx, step):
            if step - 1 <= stones[-1] - stones[stone_idx] <= step + 1:
                return True

            for i in range(stone_idx + 1, len(stones)):
                gap = stones[i] - stones[stone_idx]
                if step - 1 <= gap <= step + 1 and dfs(i, gap):
                    return True
                elif gap > step + 1:
                    break
            return False
        return dfs(1, 1)