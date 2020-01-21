# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Keep track of an interval [begin, end], in which 'furthest' tracks the largest
        index we can reach by i + nums[i].
        Once i reaches the end, we need to make a jump, and the new end is updated with
        furthest as the next reachable-by-jumping position.
        '''
        ans = 0
        furthest = 0
        curEnd = 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == curEnd:
                ans += 1
                curEnd = furthest
        return ans