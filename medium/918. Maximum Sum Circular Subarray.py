class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int

        This is based on 53. Maximum Subarray.
        There are 2 cases in general - whether or not the max subarray is circular.
        1. max subarray is no circular, so it's the same as 53;
        2. max subarray is circular, it seems tricky to handle the circle, but we can view it
            as the {sum - min_subarray_sum};
        (3). this is the edge case: if all numbers are negative, we should return #1; We can check myMax to tell
            whether all numbers are negative.
        """
        myMax = myMin = A[0]
        mySum = currentMax = currentMin = 0
        for a in A:
            mySum += a
            currentMax = max(currentMax + a, a)
            myMax = max(myMax, currentMax)
            currentMin = min(currentMin + a, a)
            myMin = min(myMin, currentMin)
        return max(myMax, mySum - myMin) if myMax > 0 else myMax