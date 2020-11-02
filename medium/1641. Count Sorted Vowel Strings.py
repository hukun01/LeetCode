# 1641. Count Sorted Vowel Strings
class Solution:
    def countVowelStrings(self, n: int) -> int:
        '''
        1/2 Math.
        Imagine we are filling a n-elelment array with these 5 letters.
        We need to make 5 sections from the array, so that the letters
        can be placed in order.
        We need 4 separators. There are (n + 4) options to place these 4 separators.
        Before the 1st separator we put 'a', between the 1st and the 2nd
        separators we put 'e', and so on.
        '''
        k = 5
        num_separator = k - 1
        return math.comb(n + num_separator, num_separator)
        '''
        2/2 DP.
        A bit better than complete brute force. Maybe more intuitive.
        '''
        @lru_cache(None)
        def dfs(prev, size):
            if size == n:
                return 1
            if prev == 5:
                return 0
            if prev < 0:
                new = 0
            else:
                new = prev
            ans = 0
            for nxt in range(new, 5, 1):
                ans += dfs(nxt, size + 1)
            return ans
        return dfs(-1, 0)