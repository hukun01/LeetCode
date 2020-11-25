# 1659. Maximize Grid Happiness
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, I: int, E: int) -> int:
        '''
        DP with state compression.
        Each cell has 3 states: empty, introvert, extrovert. We use a base 3 integer
        to represent a cell, with 0, 1, 2 mapping to each state, respectively.
        Each row is only related to its last row, in terms of the final score, so we
        enumerate all possible states for each row and its last row, and get the score.
        There's also a limit on the total number of intro and extro persons, so we need
        to consider the current count of each types in the state.

        Let f[r][i][e][curr_state] be the current max score, for the first 'r' rows, with
        'i' total intro and 'e' total extro, and 'curr_state' assignment.
        f[r][i][e][curr_state] = max(f[r-1][i'][e'][prev_state]) where i' <= a, e' <= e.
        
        The answer will be max from f[m][x][x][x] where x can be anything.
        Time: m * I * E * (3^n) where I, E is the count of intro, extro, respectively.
        Space: m * I * E * (3^n).
        A few places for optimizations:
        1. swap m and n so that 3^n is smaller.
        2. pre-compute the added score from (prev_state, curr_state).
        3. pre-compute the number of people from a state.
        '''
        ans = 0
        t = min(m, n)
        IV, EV = 120, 40
        effects = [[-60, -10, 0], [-10, 40, 0], [0, 0, 0]]
        dp = {(I, E, int(pow(3, t)) - 1): 0}
        T3 = int(pow(3, t - 1))
        for _ in range(m * n, 0, -1):
            nextdp = Counter()
            for (i, e, row), v in dp.items():
                if not i and not e:
                    ans = max(ans, v)
                    continue
                other, down = divmod(row, 3)
                right = 2 if _ % t == 0 else (row // T3)
                emptyroom = (i, e, other + 2 * T3)
                nextdp[emptyroom] = max(v, nextdp[emptyroom])
                if i:
                    introom = (i - 1, e, other)
                    nextdp[introom] = max(v + IV + effects[0][down] + effects[0][right], nextdp[introom])
                if e:
                    extroom = (i, e - 1, other + T3)
                    nextdp[extroom] = max(v + EV + effects[1][down] + effects[1][right], nextdp[extroom])
            dp = nextdp
            if not dp:
                break
        if dp:
            ans = max(ans, max(dp[_] for _ in dp ))
        return ans