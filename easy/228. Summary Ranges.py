class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        The key is to manage the boundaries accurately, and do not
        take extra space to store the interval.
        '''
        ans = []
        i = 0
        n = len(nums)
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[j - 1] + 1:
                j += 1
            if j - 1 < n and j - i >= 2:
                ans.append(f"{nums[i]}->{nums[j-1]}")
            else:
                ans.append(f"{nums[i]}")
            i = j
        
        return ans
