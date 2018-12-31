class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int

        This is based on 53. Maximum Subarray.
        There are 3 cases: 
        1. max subarray is no circular, so it's the same as 53;
        2. max subarray is circular, it seems tricky to handle the circle, but we can view it
            as the {sum - min_subarray_sum};
        3. this is the edge case, if all numbers are negative, fall back to #1, because #2 will
            be greater than #1, but that's not the correct answer. Otherwise, we should return 
            the greater one from #1 and #2;
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