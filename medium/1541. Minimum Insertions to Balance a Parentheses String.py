# 1541. Minimum Insertions to Balance a Parentheses String
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        When seeing a right paren, try to find two right parens,
        if can't find enough, we need to insert it, otherwise use both
        right parens and advance the index.
        Note that the two right parens must be adjacent, so if the input
        is "()()))", the min insertion count would be 3.
        '''
        ans = unmatched_left = 0
        n = len(s)
        i = -1
        while (i := i + 1) < n:
            if s[i] == '(':
                unmatched_left += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1
                # now we have 2 right parens, need to use a left paren or insert one.
                if unmatched_left > 0:
                    unmatched_left -= 1
                else:
                    ans += 1
        ans += unmatched_left * 2
        return ans