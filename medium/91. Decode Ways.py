class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Use ways[i] to denote the number of ways to decode s[:i]
        ways[i] += ways[i-1] if s[i-1:i] is in [1, 9]
        ways[i] += ways[i-2] if s[i-2:i] is in [10, 26] NOT [1, 26]!
        '''
        if not s:
            return 0
        ways = [0] * (len(s) + 1)
        ways[0] = 1
        for i in range(1, len(ways)):
            if 1 <= int(s[i-1:i]) <= 9:
                ways[i] += ways[i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                ways[i] += ways[i-2]
        return ways[-1]
        '''
        Note that above ways[i] is based on ways[i-1] and ways[i-2], so we can use constant space
        instead of keeping ways array.
        '''
        if not s:
            return 0
        ways1 = 1
        ways2 = 0
        ways = 0
        for i in range(1, len(s)+1):
            ways = 0
            if 1 <= int(s[i-1:i]) <= 9:
                ways += ways1
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                ways += ways2
            ways1, ways2 = ways, ways1
        return ways