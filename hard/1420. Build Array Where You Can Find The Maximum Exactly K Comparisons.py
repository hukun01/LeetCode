# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        '''
        Let f[i][j][k] be the answer, number of ways to have a sequence with
        length being n, current max being j, and has k search cost.
        
        State transition:
        f[i][j][c] += j * f[i-1][j][c], because if we have (i-1)-length array,
        we can add anything from [1, j] as the i-th number.
        f[i][j][c] += SUM of f[i - 1][x][c - 1] where x in [1, j), because
        if we have arrays with (i-1) length and x from [1, j) as the current max,
        to build the c-th search cost, we can append element j to all those arrays.
        '''
        
        MOD = 10 ** 9 + 7

        # 1/3 Regular DP as described above
        f = [[[0] * (k + 1) for j in range(m + 1)] for i in range(n + 1)]
        for j in range(1, m + 1):
            f[1][j][1] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for c in range(1, k + 1):
                    s = j * f[i-1][j][c]
                    s += sum(f[i - 1][x][c - 1] for x in range(1, j))
                    f[i][j][c] = (f[i][j][c] + s) % MOD
        
        return sum(f[n][j][k] for j in range(1, m + 1)) % MOD

        # 2/3 Space optimized DP. Note that f[i] only depends on f[i-1], so
        # we can reduce space from 3D to 2D. No change to time complexity.

        A = [[0] * (k + 1) for _ in range(m + 1)]

        for j in range(1, m + 1):
            A[j][1] = 1

        for _ in range(n - 1):
            B = [[0] * (k + 1) for _ in range(m + 1)]

            for j in range(1, m + 1):
                for c in range(1, k + 1):
                    s = j * A[j][c]
                    s += sum(A[x][c - 1] for x in range(1, j))
                    B[j][c] = s % MOD
            A = B

        return sum(A[j][k] for j in range(1, m + 1)) % MOD

        # 3/3 Further optimized time
        A = [[0] * (k + 1) for _ in range(m + 1)]

        for j in range(1, m + 1):
            A[j][1] = 1

        for _ in range(n - 1):
            B = [[0] * (k + 1) for _ in range(m + 1)]

            for c in range(1, k + 1):
                z = 0
                for j in range(1, m + 1):
                    B[j][c] = (z + j * A[j][c]) % MOD
                    z = (z + A[j][c - 1]) % MOD
            A = B

        return sum(A[j][k] for j in range(1, m + 1)) % MOD