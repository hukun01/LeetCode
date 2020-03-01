class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        1/2 Subset sum problem.
                                sum(P) - sum(N) = target
        sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                            2 * sum(P) = target + sum(nums)
        
        total = sum(nums)
        if (S + total) % 2 == 1 or total < S:
            return 0
        target = (S + total) // 2
        
        # in the first i numbers, to achieve a sum j, we have
        # ways[i][j] = ways[i-1][j] + ways[i-1][j-num], 
        # because ways[i][j] uses last row ways[i-1], we can use a 1D array to represent ways.
        ways = [0 for _ in range(target + 1)]
        ways[0] = 1
        
        for n in nums:
            for i in reversed(range(n, target+1)):
                ways[i] += ways[i - n]
        return ways[-1]

        2/2 DFS with memoization
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
                waysIfAdd = dfs(start + 1, runningSum + nums[start], seen)
                waysIfMinus = dfs(start + 1, runningSum - nums[start], seen)
                seen[mark] = waysIfAdd + waysIfMinus
            return seen[mark]
        
        return dfs(0, 0, dict())