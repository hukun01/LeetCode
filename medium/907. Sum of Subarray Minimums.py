# 907. Sum of Subarray Minimums
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        Mono stack.

        Similar to 84. Largest Rectangle in Histogram.
        Here, instead of computing the max area, we compute the number of
        subarrays whose min is 'prev_val'. This number is 'left' * 'right',
        where 'left' is the number of subarrays whose min is 'prev_val' and
        ends at 'prev_i';
        'right' is the number of subarrays whose min is 'prev_val' and starts
        at 'prev_i'.

        Time: O(n)
        Space: O(n)
        '''
        stack = []
        ans = 0
        for i, a in enumerate(arr + [0]):
            start = i
            while stack and stack[-1][0] >= a:
                prev_val, prev_start, prev_i = stack.pop()
                left = prev_i - prev_start + 1    
                right = i - prev_i
                ans += prev_val * left * right
                start = prev_start
            stack.append((a, start, i))

        return ans % (10 ** 9 + 7)