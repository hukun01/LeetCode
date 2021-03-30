# 873. Length of Longest Fibonacci Subsequence
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        '''
        DP.

        Let f[j, k] be the longest subsequence that ends at A[j] and A[k].
        f[j, k] = f[i, j] + 1 if f[i] + f[j] == nums[k], for all j < k.

        Since the values are unique, we use a mapping to record their indicies,
        and use that to quickly locaet the f[i].
        Note that we need to check i < j.

        Time: O(n^2)
        Space: O(n)
        '''
        index = {x: i for i, x in enumerate(A)}
        longest = defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0