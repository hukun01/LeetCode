class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        DFS with memoization
        '''
        def dfs(start, runningSum, seen):
            if start == len(nums):
                if runningSum == S:
                    return 1
                return 0
                
            # this is used to mark the starting index and runningSum and 
            # the number of possible ways from here
            mark = str(start) + "->" + str(runningSum)
            if mark not in seen:
                waysIfAdd = dfs(start + 1, runningSum - nums[start], seen)
                waysIfMinus = dfs(start + 1, runningSum + nums[start], seen)
                seen[mark] = waysIfAdd + waysIfMinus
            return seen[mark]
        
        return dfs(0, 0, dict())