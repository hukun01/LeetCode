# 678. Valid Parenthesis String
class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        1/2 Memoized DFS is straightforward and fast enough to pass, but
        there is another solution with much better time and space complexities.
        '''
        @lru_cache(None)
        def dfs(i, left):
            for j in range(i, len(s)):
                if s[j] == '(':
                    left += 1
                elif s[j] == ')':
                    if left == 0:
                        return False
                    left -= 1
                else:
                    ans = dfs(j + 1, left) or dfs(j + 1, left + 1)
                    if ans or left > 0 and dfs(j + 1, left - 1):
                        return True
            return left == 0
        return dfs(0, 0)
        '''
        2/2 DFS without actually searching.
        We just want to know *whether* it's possible to be valid, we don't need
        to know what exact steps to use stars to make the string valid.

        Hence, we keep track of the relative count of left parenthesis, and we record
        its range - what the lower and upper bound is as we go through the string.

        Use left paren as the base, when we see a right paren, we decrement the count,
        then it's possible to have a valid string if the lower bound is 0, and upper bound >= 0.

        On the other hand, whenever the upper bound becomes negative, it means no matter how we
        use stars as as left parens, the right ones outnumber the left, and it's impossible to
        get a valid string.

        Below code can be refactored to make shorter, but it would be less clear.
        '''
        # lower is the smallest possible relative count of left parens
        # upper is the largest possible relative count of left parens
        lower = upper = 0
        for c in s:
            if c == '(':
                lower += 1
                upper += 1
            elif c == ')':
                if lower > 0:
                    lower -= 1
                upper -= 1
                if upper < 0:
                    return False
            else:
                if lower > 0:
                    lower -= 1
                upper += 1
        return lower == 0