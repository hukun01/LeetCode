# 1655. Distribute Repeating Integers
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        '''
        DP.
        There are at most m (10) customers, so the number of states where
        different customers are satisfied is 2^10.
        Also, we will count the frequencies of the nums, and there are at
        most 50 unique values.
        These numbers are small enough that we can enumerate all states
        and check whether the first i freqs can satisfy each state.

        The transition functions are
        f[i][state] = f[i-1][state] or any(f[i-1][sub_state] and (i-1)th
        freq can satisfy (state - sub_state), where sub_state is a subset

        And the answer would be f[N][final_state] where N is len(freqs).
        of state).

        Time: O(N * 3^m) as there are C(m, k) states with k bits being 1,
        and each state has 2^k sub_states. The total is ∑_(0, m)(C(m, k) * 2^k),
        which is (2 + 1)^m, based on binomial theorem. Check this link
        for reference: https://cp-algorithms.com/algebra/all-submasks.html
        Space: O(N * 2 ^ m).

        Note that we must pre-compute the sums for all possible state, this
        is to reduce O(m) from time, otherwise it will TLE.
        '''
        freqs = list(Counter(nums).values())
        N = len(freqs)
        m = len(quantity)
        
        state_sum = Counter()
        for state in range(1 << m):
            for i in range(m):
                if (state >> i) & 1:
                    state_sum[state] += quantity[i]

        f = [[False] * (1 << m) for _ in range(N + 1)]
        for i in range(N + 1):
            f[i][0] = True

        for i in range(1, N + 1):
            for state in range(1 << m):
                f[i][state] = f[i-1][state]
                subset = state
                while subset and not f[i][state]:
                    if f[i-1][state - subset] and state_sum[subset] <= freqs[i-1]:
                        f[i][state] = True
                    subset = (subset - 1) & state
        return f[N][(1 << m) - 1]