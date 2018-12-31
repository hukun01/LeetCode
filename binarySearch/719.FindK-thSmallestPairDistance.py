class Solution:
    def smallestDistancePair(self, nums, k):
        """
        Another instance for binary searching the value spaces. 
        Make sure to sort the list if it's not sorted, so to make the pairs counting run in linear time.

        Total runtime is the bigger one between O(n * log(max - min)) and O(n * log(n))

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def countPairs(nums, maxDistance):
            j, count = 0, 0
            # each time j gets bigger, so the runtime would be (n + n), aka, O(n)
            for i in range(len(nums)):
                while j < len(nums) and nums[j] <= nums[i] + maxDistance:
                    j += 1
                count += j - i - 1
            return count
            
        nums.sort()
        l, h = 0, nums[-1] - nums[0]
        while l < h:
            m = (l + h) // 2
            if countPairs(nums, m) < k:
                l = m + 1
            else:
                h = m
        return l