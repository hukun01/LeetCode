# 691. Stickers to Spell Word
from collections import Counter, defaultdict
from math import inf, isinf
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickCounters = list(map(Counter, stickers))
        dp = defaultdict(lambda: inf, {(): 0})
        def dfs(count):
            i = tuple(count.items())
            if isinf(dp[i]):
                for sCount in stickCounters:
                    if sCount[i[0][0]] > 0:
                        dp[i] = min(dp[i], 1 + dfs(count - sCount))
            return dp[i]
        
        # ':=' is assignment within expression, this is newly supported since Py 3.8.
        return -1 if isinf(ans := dfs(Counter(target))) else ans