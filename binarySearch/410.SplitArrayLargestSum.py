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
        def isPossible(nums, m, threshold):
            count = 0
            i = 0
            while i < len(nums) and count <= m:
                runningSum, j = 0, i
                while j < len(nums) and runningSum + nums[j] <= threshold:
                    runningSum += nums[j]
                    j += 1
                i = j
                count += 1
                
            return count <= m
        
        l, h = max(nums), sum(nums)
        while l < h:
            mid = (l + h) // 2
            if isPossible(nums, m, mid):
                h = mid
            else:
                l = mid + 1
        
        return l