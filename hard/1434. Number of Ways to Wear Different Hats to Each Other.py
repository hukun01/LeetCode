# 1434. Number of Ways to Wear Different Hats to Each Other
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        '''
        DP with state compression.
        The key is to let the hat choose the person, not vice versa, because the
        number of hats is much greater than that of persons.
        1/2 Iterative, much faster than 2/2.
        '''
        hatToPerson = collections.defaultdict(list)
        for p, hs in enumerate(hats):
            for h in hs:
                hatToPerson[h].append(p)

        MOD = 10 ** 9 + 7
        N = len(hats)
        target = (1 << N) - 1
        f = [0] * (target + 1)
        f[0] = 1
        for h in hatToPerson:
            for assignment in range(target, -1, -1):
                for p in hatToPerson[h]:
                    if assignment & (1 << p) != 0:
                        f[assignment] += f[assignment ^ (1 << p)]
        return f[-1] % MOD
        '''
        2/2 DFS with memoization.
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
                            ans += dp(currAssigned | (1 << person), h)
            return ans % MOD
        
        return dp(0, 0)