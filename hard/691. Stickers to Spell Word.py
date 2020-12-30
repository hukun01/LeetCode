# 691. Stickers to Spell Word
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        '''
        DP.
        Let dp[i] be the min number of stickers that make up state i, where
        a state is a tuple of ((char1, needed_count1), (char2, ..), ..).
        We have dp[()] = 0, and dp[i] = min(1 + dp[x]) where x is the new
        state after 'i' is applied by some sticker.
        To optimize/prune, we require that the next sticker must contain the
        first char in current state, as there must be some sticker that does
        in any feasible answer. This way we reduce lots of search paths that
        lead to the same result.

        Time: O(2^T * S * T) where T is len(target), S is len(stickers). This
              is the time bound for brute force style DP, with optimization
              and prune in this solution, the time is shorter.
        Space: O(2^T)
        '''
        sticker_counters = [Counter(s) for s in stickers]
        dp = defaultdict(lambda: inf, {(): 0})
        def dfs(need):
            i = tuple(need.items())
            if isinf(dp[i]):
                for s in sticker_counters:
                    if s[i[0][0]] > 0:
                        dp[i] = min(dp[i], 1 + dfs(need - s))
            return dp[i]

        return -1 if isinf(ans := dfs(Counter(target))) else ans