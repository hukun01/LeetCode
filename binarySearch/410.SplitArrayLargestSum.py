class Solution:
    def splitArray(self, nums, m):
        """
        Another instance of value search.
        Why are you sure that the final l will be the correct answer?
        Whenever we find a smaller good value, we set it as the inclusive upper bound; 
        whenever we find a bad value that’s too small, we set it as the exclusive lower bound. 
        Thus, we will eventually tighten up the search space until it contains only one good value which will be the smallest one.
        
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplitWith(threshold):
            count = 1
            runningSum = 0
            for num in nums:
                if runningSum + num <= threshold:
                    runningSum += num
                else:
                    runningSum = num
                    count += 1
            return count <= m
        
        l, h = max(nums), sum(nums)
        while l < h:
            mid = (l + h) // 2
            if canSplitWith(mid):
                h = mid
            else:
                l = mid + 1
        
        return l