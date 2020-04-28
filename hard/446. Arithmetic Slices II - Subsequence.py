# 446. Arithmetic Slices II - Subsequence
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        total = 0
        dp = [collections.defaultdict(int) for _ in A]
        for end in range(len(A)):
            for last in range(end):
                delta = A[end] - A[last]
                dp[end][delta] += 1
                dp[end][delta] += dp[last][delta]
                total += dp[last][delta]
        return total