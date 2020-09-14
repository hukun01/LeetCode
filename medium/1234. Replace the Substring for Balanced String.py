# 1234. Replace the Substring for Balanced String
class Solution:
    def balancedString(self, s: str) -> int:
        '''
        Sliding window.
        Find all chars with extra count.
        Have a sliding window, in which we erase all chars.
        The window goes right until all extra chars are erased.
        Start shrinking the window from left, and add chars back.
        If the added chars don't become extra, we have a smaller window.
        '''
        n = len(s)
        equal = n // 4
        extra = { char: count - equal for char, count in Counter(s).items() if count > equal }

        count = len(extra)
        if count == 0:
            return 0

        result = math.inf
        l = r = 0
        while r < n:
            if s[r] in extra:
                extra[s[r]] -= 1
                if extra[s[r]] == 0:
                    count -= 1
            r += 1
            
            while count == 0:
                if s[l] in extra:
                    extra[s[l]] += 1
                    if extra[s[l]] > 0:
                        count += 1
                l += 1

                result = min(result, r - l + 1)
        return result