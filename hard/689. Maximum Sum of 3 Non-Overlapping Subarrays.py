# 689. Maximum Sum of 3 Non-Overlapping Subarrays
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        '''
        Sliding window + DP - a general approach.
        Maintain m sliding windows, where m is the number of subarrays.
        In this problem, m = 3.
        Keep moving all sliding windows and keep track of their current sums.
        Find the i-th best sums based on the (best_sums[i-1] + cur_sums[i]).
        '''
        m = 3
        idx = []
        best_idx = []
        for i in range(0, k * (m - 1) + 1 ,k):
            idx.append(i)
            best_idx.append(idx[:])

        # Sums of each window
        cur_sums = []
        prev = 0
        for cut in range(k, k*m + 1, k):
            cur_sums.append(sum(nums[prev:cut]))
            prev = cut

        # Sums of combined best windows
        best_sums = list(itertools.accumulate(cur_sums))

        # Current window positions
        win_idx = [i for i in range(1, k * (m-1) + 2, k)]
        while win_idx[m-1] <= len(nums) - k:
            # Update the three sliding windows
            for i in range(m):
                cur_sums[i] += nums[win_idx[i] + k - 1] - nums[win_idx[i] - 1]
            
            # Update best single window
            if cur_sums[0] > best_sums[0]:
                best_idx[0] = [win_idx[0]]
                best_sums[0] = cur_sums[0]
            for i in range(1, m):
                if (cur_sum := best_sums[i-1] + cur_sums[i]) > best_sums[i]:
                    best_idx[i] = best_idx[i-1] + [win_idx[i]]
                    best_sums[i] = cur_sum

            win_idx = [i + 1 for i in win_idx]

        return best_idx[m-1]