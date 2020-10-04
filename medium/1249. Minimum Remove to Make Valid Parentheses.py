# 1249. Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        1/2 Array scan once.
        Keep track of all left paren index, and remove one per right paren.
        Record the index where extra right paren present, and merge it with
        the extra left paren index.
        All chars that are not on extra index can be removed at the end.
        '''
        lefts = []
        removes = set()
        for i, c in enumerate(s):
            if c == '(':
                lefts.append(i)
            elif c == ')':
                if lefts:
                    lefts.pop()
                else:
                    removes.add(i)
        removes |= set(lefts)
        return ''.join(c for i, c in enumerate(s) if i not in removes)

        '''
        2/2 Scan the character array twice.
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