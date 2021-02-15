# 1027. Longest Arithmetic Subsequence
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        '''
        DP.
        Let f[i, d] be the length of arithmetic subsequence ended at index 'i'
        with difference 'd'
        At index 'j', d = A[j] - A[i], f[j, d] = f[i, d] + 1 if f[i, d] exists.

        Note that by default an element is arithmetic sequence with length 1.

        Time: O(n ^ 2)
        Space: O(n ^ 2)
        '''
        dp = defaultdict(lambda: 1)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                delta = A[j] - A[i]
                dp[j, delta] = dp[i, delta] + 1
        return max(dp.values())