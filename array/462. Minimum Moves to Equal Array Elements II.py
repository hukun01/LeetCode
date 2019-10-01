class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        '''
        From two sets of points, the median is the point where we can reach both sides in the minimum total distance.
        '''
        nums.sort()
        if len(nums) % 2 == 1:
            target = nums[len(nums) // 2]
        else:
            target = math.ceil((nums[len(nums) // 2] + nums[(len(nums)-1) // 2]) / 2)
        return sum(abs(target - n) for n in nums)