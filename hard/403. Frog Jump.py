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
        '''
        2/2 Dict + BFS.
        '''
        stone_steps = { stone: set() for stone in stones }
        stone_steps[0].add(0)
        for stone in stones:
            for k in stone_steps[stone]:
                for step in range(max(1, k - 1), k + 2):
                    if (next_step := stone + step) in stone_steps:
                        stone_steps[next_step].add(step)
                        if next_step == stones[-1]:
                            return True
        return False