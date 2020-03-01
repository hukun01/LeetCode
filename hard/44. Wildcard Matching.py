# 44. Wildcard Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Similar to 10. Regular Expression Matching
        
        We start the comparison from tail.
        '''
        cache = {}
        def match(sIdx, pIdx):
            if (sIdx, pIdx) in cache:
                return cache[(sIdx, pIdx)]
            if sIdx == -1:
                if pIdx == -1:
                    return True
                elif p[pIdx] == '*':
                    return match(sIdx, pIdx - 1)
                return False
            if pIdx == -1:
                return False
            result = False
            if s[sIdx] == p[pIdx] or p[pIdx] == '?':
                result |= match(sIdx - 1, pIdx - 1)
            if p[pIdx] == '*':
                # current * match anything
                result |= match(sIdx - 1, pIdx)
                # current * match nothing
                result |= match(sIdx, pIdx - 1)
            cache[(sIdx, pIdx)] = result
            return result
            
        return match(len(s) - 1, len(p) - 1)