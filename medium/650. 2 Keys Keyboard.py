# 650. 2 Keys Keyboard
class Solution:
    def minSteps(self, n: int) -> int:
        '''
        DP.
        1st thought:
        * O(n^2) time and O(n) space
        dp[i] represents the min number of steps to get i 'A'.
        There are two operations:
        1) paste -> 1 step
        2) copy all, then paste -> 2 steps
        
        State Transition:
        dp[i] = min(dp[j] + 1 + x), where j == i // (x + 1),
        also, '1' means 'copy dp[j]', and 'x' means 'paste dp[j] x times'.

        For example:
        dp[2] = dp[1] + 1 + 1, where 1 == 2 // (1 + 1)
        dp[123]=dp[41]+ 1 + 2, where 41==123// (2 + 1)
        
        2nd thought:
        * O(n) time and space
        To optimize, we can explore x from the smallest possible value,
        the first x will be the best option.
        
        3rd thought: 
        * Best case O(log(n)) time, and space, worst case O(n) both.
        For a given number n, we don't have to compute all results in [1, n],
        but just need the relevant dp[n], dp[j], ..., etc.
        Hence we can do this from backwards with memorized dfs.
        
        4th thought:
        * Best case O(log(n)) time, O(1) space
        We don't even need to memorize the intermediate result if we can
        build the result from bottom up. We can translate the below backward
        dfs logic into forward while loop logic.
        '''
        dp = {}
        dp[0] = dp[1] = 0
        def dfs(n):
            if n in dp:
                return dp[n]
            for x in range(1, n):
                if n % (x + 1) == 0:
                    j = n // (x + 1)
                    dp[n] = dfs(j) + 1 + x
                    return dp[n]
        return dfs(n)
        '''
        
        ans = 0
        for d in range(2, n + 1):
            while n % d == 0:
                ans += d
                n //= d
        return ans
        '''