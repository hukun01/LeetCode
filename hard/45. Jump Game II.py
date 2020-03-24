# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Keep track of an interval [begin, end], in which 'furthest' tracks the largest
        index we can reach by i + nums[i].
        Once i reaches the end, we need to make a jump, and the new end is updated with
        furthest as the next reachable-by-jumping position.
        Similar to 1024. Video Stitching.
        '''
        ans = furthest = currEnd = i = 0
        while currEnd < len(nums) - 1:
            while i <= currEnd:
                furthest = max(furthest, nums[i] + i)
                i += 1
            currEnd = furthest
            ans += 1
        return ans
        
        '''
        Another style.
        '''
        ans = furthest = currEnd = 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == currEnd:
                ans += 1
                currEnd = furthest
        return ans