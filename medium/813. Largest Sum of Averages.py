# 813. Largest Sum of Averages
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        '''
        1/2 Top down DFS with memoization

        2/2 Bottom up DP with preprocessed prefix sums array.
        Note that prefix sums array can be useful in dealing with interval sums.
        '''
        @lru_cache(None)
        def dfs(i, k):
            if i == len(A):
                return 0
            if k == 1:
                return sum(A[i:]) / (len(A) - i)
            total = 0
            runningSum = 0
            for j in range(i, len(A)):
                runningSum += A[j]
                total = max(total, dfs(j+1, k-1) + runningSum / (j - i + 1))
            return total
        return dfs(0, K)