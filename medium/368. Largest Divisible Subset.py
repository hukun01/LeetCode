# 368. Largest Divisible Subset
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        1/2 DP, similar to LIS.
        Let f[a] be the largest divisible subset that contains a, then we have
            f[a] = max([f[b] for b in f if a % b == 0], key=len) | {a}
        In above transition function, b is the max element in its subset.
        Hence, we sort the nums to ensure all its possible divisor appear
        before the elelment. And we don't need to check every other elements
        in the subset.

        Note that we initialize f with { -1: set() } to ensure max() returns
        at least an empty set.

        Time: O(n^2)
        Space: O(n^2)
        '''
        f = { -1: set() }
        for a in sorted(nums):
            f[a] = max([f[k] for k in f if a % k == 0], key=len) | {a}
        return list(max(f.values(), key=len))
        '''
        2/2 DP, with less space.
        Instead of tracking all subsets with O(n^2) space, we can track only
        the size like LIS, and after it, find the max size and its index.
        Then, traverse the nums reversely, from the max index to 0, add the
        value to the result, when f[i] == cur_size and cur_tail % nums[i] == 0.
        This works because f[i]'s subset ends with nums[i].

        Time: O(n^2)
        Space: O(n)
        '''
        n = len(nums)
        if n == 0:
            return []
        f = [0] * n
        nums.sort()
        for i, a in enumerate(nums):
            f[i] = max([f[j] for j in range(i) if nums[i] % nums[j] == 0] + [0]) + 1
        max_size, max_idx = max([(v, i) for i, v in enumerate(f)])

        ans = []
        cur_size, cur_tail = max_size, nums[max_idx]
        for i in range(max_idx, -1, -1):
            if cur_size == f[i] and cur_tail % nums[i] == 0:
                ans.append(nums[i])
                cur_size -= 1
                cur_tail = nums[i]
        return ans