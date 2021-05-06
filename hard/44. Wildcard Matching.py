# 44. Wildcard Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Similar to 10. Regular Expression Matching
        
        We start the comparison from tail.
        '''
        @cache
        def match(i, j):
            if j == -1:
                return i == -1
            ans = False
            if p[j] == '*':
                if i >= 0:
                    ans |= match(i - 1, j)
                ans |= match(i, j - 1)
            if i >= 0 and p[j] in ('?', s[i]):
                ans |= match(i - 1, j -1)
            return ans
        return match(len(s) - 1, len(p) - 1)

        '''
        A faster method.
        '''
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1
 
        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1 
            elif star_idx == -1:
                return False
            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        
        return all(x == '*' for x in p[p_idx:])