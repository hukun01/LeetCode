# 1690. Stone Game VII
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        '''
        Interval DP.
        There's no difference between Alice's goal and Bob's goal, they both
        try to maximize (alice_score - bob_score). Hence, we can use one
        recursion to return the max diff. Note that this is different from each
        person trying to maximize his own score.
        The recursion returns the max diff in [l, r] between current player and
        the other. Let diff() be the recursion, aka, the total diffs bewteen
        Alice and Bob. As Alice plays first, we have below:
        diff() = alice_current_round_score - diff(Bob - Alice)
            = alice_current_round_score - (bob_total_score - alice_rest_score)
            = alice_current_round_score + alice_rest_score - bob_total_score
            = alice_total_score - bob_total_score
        Same applies when Bob plays first in the subarray.

        One key is to call cache_clear() at the end, or do lru_cache(1000*2).
        Otherwise it will TLE due to memory consumption.

        Time: O(n^2) where n is len(stones)
        Space: O(n^2)
        '''
        pre = [0] + list(accumulate(stones))
        def get_range_sum(l, r):
            return pre[r + 1] - pre[l]
        @cache
        def get_diff(l, r):
            if l == r:
                return 0
            return max(
                get_range_sum(l + 1, r) - get_diff(l + 1, r),
                get_range_sum(l, r - 1) - get_diff(l, r - 1))
        ans = get_diff(0, len(stones) - 1)
        get_diff.cache_clear()
        return ans