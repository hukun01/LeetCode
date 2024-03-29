class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Iterate through the nums, for each index, do 3sum on nums[i+1:].
        Note that to dedup, we don't need to use set(), but just need to
        skip the same element after using it once in 3sum.

        To improve runtime performance, we can add pruning logic to early
        stop/skip some iteration. See the commented lines. Those two blocks
        can improve the runtime from 40% to 90% on the ranking.
        ''' 
        nums.sort()

        def threeSum(start, array, target):
            result = []
            if target < array[start] * 3 or target > array[-1] * 3:
                return result
            for m in range(start, len(array) - 2):
                if m > start and nums[m] == nums[m - 1]:
                    continue
                l = m + 1
                r = len(array) - 1
                newTarget = target - array[m]
                ''' perf only
                if newTarget < 2 * array[m]:
                    break
                if newTarget > 2 * array[-1]:
                    continue
                '''
                while l < r:
                    s = array[l] + array[r]
                    if s == newTarget:
                        result.append([array[m], array[l], array[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < newTarget:
                        l += 1
                    else:
                        r -= 1

            return result

        ans = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ''' perf only
            if 4 * nums[i] > target:
                break
            if nums[i] + 3 * nums[-1] < target:
                continue
            '''
            for subAns in threeSum(i + 1, nums, target - nums[i]):
                ans.append([nums[i], *subAns])
        return ans