# 1639. Number of Ways to Form a Target String Given a Dictionary
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        '''
        DP.
        Let f[i][j] be the number of ways to get the first j chars in target,
        using the first i columns in words.
        f[i][j] = sum of items below:
            1. f[i-1][j]
                this means in the first (i-1) columns we can get j chars.
            2. f[i-1][j-1] * (number of char target[j-1] in column i-1)
                this means in the first (i-1) columns we can get (j-1) chars,
                and the j-th char is taken from the i-th column.
        Note that the index is shifted +1, to handle initial case.
        '''
        MOD = 10 ** 9 + 7
        w = len(words[0])
        t = len(target)
        if t > w:
            return 0
        f = [[0] * (t + 1) for _ in range(w + 1)]
        f[0][0] = 1
        for k in range(1, w + 1):
            freqs = Counter()
            for word in words:
                freqs[word[k-1]] += 1
            f[k][0] = 1
            for i in range(1, t + 1):
                f[k][i] = f[k-1][i] + f[k-1][i-1] * freqs[target[i-1]]
                f[k][i] %= MOD
        return f[w][t]