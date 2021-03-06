# 1626. Best Team With No Conflicts
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        '''
        DP.
        Sort the players by age, because this will let us not worry about
        age when checking players.
        Let f[i] be the max scores for the first i players, we have
        f[i] = max(f[j] + scores[i] for j
            where ages[j] <= ages[i] and scores[j] <= scores[i])
        We can now simply check whether scores[j] <= scores[i] for j in [0, i),
        because we already sorted by age.
        '''
        players = sorted((a, s) for a, s in zip(ages, scores))
        n = len(ages)
        f = [0] * n
        for i, (_, score) in enumerate(players):
            f[i] = score  # base case, where we start with current player.
            for j in range(i):
                if players[j][1] <= score:
                    f[i] = max(f[i], f[j] + score)
        return max(f)