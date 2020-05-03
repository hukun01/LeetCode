# 1434. Number of Ways to Wear Different Hats to Each Other
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        '''
        DP with state compression.
        The key is to let the hat choose the person, not vice versa, because the
        number of hats is much greater than that of persons.
        '''
        MOD = 10 ** 9 + 7
        N = len(hats)
        allPersons = (1 << N) - 1
        @lru_cache(None)
        def dp(currAssigned, hat_num):
            if currAssigned == allPersons:
                return 1
            ans = 0
            for person in range(N):
                if (currAssigned >> person) & 1 == 0:
                    # try to wear hat num
                    for h in hats[person]:
                        if h > hat_num:
                            ans += dp(currAssigned ^ (1 << person), h)
            return ans % MOD
        
        return dp(0, 0)