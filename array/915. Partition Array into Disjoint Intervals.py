class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        Linear scan with 3 variables:
            1. the partition index;
            2. the max of left partition;
            3. the overall max so far as we scan.
        Scan from left to right, at each index, if the leftMax <= a, 
        the current partition is still good, we just need to update the runningMax.
        If the leftMax > a, then the current partition is not good, 
        we need to reset partitionIdx to be the current index, and reset the leftMax
        to be the runningMax.
        As it's guaranteed that there is an answer, after some partitionIdx,
        for each element a after partitionIdx, will satisfy: leftMax <= a.
        """
        leftMax = runningMax = A[0]
        partitionIdx = 0
        for i, a in enumerate(A):
            if leftMax > a:
                partitionIdx = i
                leftMax = runningMax
            else:
                runningMax = max(runningMax, a)
        return partitionIdx + 1