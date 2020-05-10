# 1425. Constrained Subsequence Sum
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        '''
        Use intuition from 239. Sliding Window Maximum.
        Let f[i] be the answer when the subsequence ends at nums[i],
        f[0] = nums[0]
        f[i] = nums[i] + x, where x = max(f[j] for all the j that i-j <= k)
        x is the max sum of previous subsequence that ends at one of the last k-1 numbers.
        If x < 0, just ignore it, which means let the subsequence start from nums[i].
        To make this process faster, we leverage the optimal solution in 239 that
        tells the max in a sliding window in constant time once the window is built.
        '''
        w = collections.deque([0])
        f = nums[:] # f[i] >= nums[i], at least.
        for i in range(1, len(f)):
            f[i] += max(f[w[0]], 0)

            # This is all from 239.
            while w and f[w[-1]] <= f[i]:
                w.pop()
            w.append(i)
            if i - w[0] >= k:
                w.popleft()
        return max(f)