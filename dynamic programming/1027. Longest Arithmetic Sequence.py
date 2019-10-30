class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[diff][index] denotes the length of arithmetic sequence at 'index' with difference 'diff'
        dp = collections.defaultdict(lambda: 1)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                delta = A[j] - A[i]
                dp[j, delta] = dp[i, delta] + 1
        return max(dp.values())