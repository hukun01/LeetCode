# 65. Valid Number
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_e = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c in 'eE':
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            elif c == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit