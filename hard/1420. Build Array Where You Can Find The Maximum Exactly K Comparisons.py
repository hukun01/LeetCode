# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        '''
        1/2 DP.
        Let f[i][j][c] be the answer, number of ways to have a sequence with
        length being i, search cost being j, current max being c.
        
        State transition:
        f[i][j][c] = item1 + item2
        item1: c * f[i-1][j][c], because if we have (i-1)-length array,
               we can add anything from [1, c] as the i-th number.
        item2: sum(f[i - 1][j - 1][1:c]), because if we have arrays with
               (i-1) length and x from [1, c) as the current max, to build
               the j-th search cost, we can append element c to all those arrays.

        Note that f[i] depends on f[i-1], so we can reduce 3D space to 2D.
        Time complexity is O(nkm^2)
        '''
        MOD = 10 ** 9 + 7

        f = [[[0] * (m + 1) for j in range(k + 1)] for i in range(n + 1)]
        for c in range(1, m+1):
            f[1][1][c] = 1
        for i in range(2, n+1):
            for j in range(1, k+1):
                for c in range(1, m+1):
                    f[i][j][c] = f[i-1][j][c] * c + sum(f[i-1][j-1][1:c])
        return sum(f[n][k][1:]) % MOD

        '''
        2/2 Optimized DP, with reduced space (2D) and time (O(nkm)).
        Space optimization is based on the fact that f[i] depends on f[i-1].

        Time optimization is based on the fact that we always get sum([1:c])
        from the last row in the deepest for loop, so we can just compute it
        once.
        '''
        f1 = [[0] * (m + 1) for j in range(k + 1)]
        f1[1][1:] = [1] * m
        for _ in range(2, n+1):
            f2 = [[0] * (m + 1) for j in range(k + 1)]
            for j in range(1, k+1):
                item2s = list(itertools.accumulate(f1[j-1]))
                for c in range(1, m+1):
                    f2[j][c] = f1[j][c] * c + item2s[c-1]
            f1 = f2
        return sum(f1[k][1:]) % MOD