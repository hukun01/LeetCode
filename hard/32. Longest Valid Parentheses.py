class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        The parens are only valid when the numbers of left and right are equal.
        
        Keep counting left and right, if left == right, we can use 2*right
        as the parens length, if right > left, the parens is broken, we need to
        reset left = right = 0.
        Also need to do the same process for the reversed string with opposite
        left and right, to handle cases like '(()'.
        '''
        def check(s, leftParen, rightParen):
            maxLen = left = right = 0
            for c in s:
                if c == leftParen:
                    left += 1
                else:
                    right += 1
                if left == right:
                    maxLen = max(maxLen, 2 * right)
                elif right > left:
                    left = right = 0
            return maxLen
        return max(check(s, '(', ')'), check(s[::-1], ')', '('))