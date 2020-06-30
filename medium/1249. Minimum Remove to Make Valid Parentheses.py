# 1249. Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Scan the character array twice.
        Similar to 32. Longest Valid Parentheses.
        '''
        chars = list(s)
        def remove_one_paren(chars, left_paren, right_paren):
            extra_open = 0
            for i, c in enumerate(chars):
                if c == left_paren:
                    extra_open += 1
                elif c == right_paren:
                    if extra_open > 0:
                        extra_open -= 1
                    else:
                        chars[i] = ''
            return chars
        left_removed = remove_one_paren(chars,'(', ')')[::-1]
        both_removed = remove_one_paren(left_removed, ')', '(')[::-1]
        return ''.join(both_removed)