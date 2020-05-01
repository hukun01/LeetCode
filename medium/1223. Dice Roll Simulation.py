# 1223. Dice Roll Simulation
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        '''
        f.
        Let f[i][j] be the number of sequences ends with j after i rolls.
        f[1] = [1] * dices, because 1 roll, 1 dice, 1 way
        f[i][j] = sums(f[i-1]) - invalid
        k = i - rollMax[j]
        invalid = sums(f[k - 1]) - f[k - 1][j]
        '''
        dices = len(rollMax)
        mod = 10**9+7
        f = [[0] * dices for _ in range(n+1)]
        f[1] = [1] * dices

        # sums[i] is the total number of ways with i rolls.
        sums = [0] * (n+1)
        sums[1] = 6

        for i in range(2, n+1):
            for j in range(dices):
                k = i - rollMax[j] # i - k <= rollMax[j]
                if k - 1 >= 1:
                    invalid = sums[k - 1] - f[k - 1][j]
                else:
                    invalid = max(k, 0)
                f[i][j] = sums[i - 1] - invalid
            sums[i] = sum(f[i]) % mod
        return sums[n]