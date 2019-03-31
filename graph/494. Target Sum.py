class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        DFS with memoization
        '''
        def findWays(nums, index, runningSum, S, mappings):
            if index == len(nums):
                if runningSum == S:
                    return 1
                else:
                    return 0

            # this is used to mark the starting index and runningSum and 
            # the number of possible ways from here
            mark = str(index) + "->" + str(runningSum)
            if mark in mappings:
                return mappings[mark]
            
            num = nums[index]
            waysIfAdd = findWays(nums, index + 1, runningSum + num, S, mappings)
            waysIfMinus = findWays(nums, index + 1, runningSum - num, S, mappings)
            mappings[mark] = waysIfAdd + waysIfMinus
            return waysIfAdd + waysIfMinus
                
        return findWays(nums, 0, 0, S, dict())