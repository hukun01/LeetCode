# 918. Maximum Sum Circular Subarray
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        This is based on 53. Maximum Subarray.
        There are 2 cases in general - whether or not the max subarray is circular.
        1. max subarray is no circular, so it's the same as 53;
        2. max subarray is circular, it seems tricky to handle the circle, but we can
           view it as the {sum - min_subarray_sum};
        (3). this is the edge case: if all numbers are negative, we should return #1;
           We can check max_sum to tell whether all numbers are negative.
        '''
        max_sum = min_sum = A[0]
        total = cur_max_sum = cur_min_sum = 0
        for a in A:
            total += a
            cur_max_sum = max(cur_max_sum + a, a)
            max_sum = max(max_sum, cur_max_sum)
            cur_min_sum = min(cur_min_sum + a, a)
            min_sum = min(min_sum, cur_min_sum)
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum