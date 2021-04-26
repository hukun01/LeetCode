# 837. New 21 Game
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        '''
        DP.

        First of all, if K == 0 or N >= K + W, we always win.

        Otherwise, K > 0 and N < K + W, and we can lose when points exceed
        N, because points is [K, K - 1 + W], this is because the game ends
        whenever we reach K, so the last but one round we can get up to
        K - 1, and the next round we can have [1, W] added points.

        Let f[i] be the probability of getting i points. Then we have
        f[i] = sum(f[i-1] + f[i-2] + ... + f[max(0, i-W)]) / W
             = Wsum / W

        Also, f[0] = 1, this pre-exists before the game.

        The range of i is [1, N] as we are only interested in points <= N.
        Naively implement above transition would be too slow O(N * W). Instead,
        we use a sliding window to track Wsum.
        Note that we can only keep adding to Wsum if i < K, because the game
        ends when i >= K.

        Time: O(N)
        Space: O(N)
        '''
        if K == 0 or N >= K + W:
            return 1

        f = [1.0] + [0.0] * N
        Wsum = 1
        for i in range(1, N + 1):
            f[i] = Wsum / W
            if i < K:
                Wsum += f[i]
            if i - W >= 0:
                Wsum -= f[i - W]
        return sum(f[K:])