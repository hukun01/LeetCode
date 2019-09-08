class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Use nums[i] to denote the number of ways to decode s[:i+1], need to handle the cases
        that s[i] == '0', and s[i-1:i+1] is not in [10, 26] (NOT [1, 26]!).
        '''
        if not s:
            return 0
        nums = [0] * len(s)
        nums[0] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if 1 <= int(s[i]) <= 9:
                nums[i] += nums[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i >= 2:
                    nums[i] += nums[i-2]
                else:
                    nums[i] += 1
        return nums[-1]
        '''
        Note that above nums[i] is based on nums[i-1] and nums[i-2], so we can use constant space
        instead of keeping nums array.
        
        if not s:
            return 0
        p1 = 1 if s[0] != '0' else 0
        p2 = 0
        for i in range(1, len(s)):
            curr = 0
            if 1 <= int(s[i]) <= 9:
                curr += p1
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i >= 2:
                    curr += p2
                else:
                    curr += 1
            p1, p2 = curr, p1
        return p1
        '''