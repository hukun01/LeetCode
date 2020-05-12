class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        1/2 Regular solution.
        Keep two mappings from s to t and t to s, make sure each char
        maps from s to t and t to s.
        '''
        mapping1 = {}
        mapping2 = {}
        for c1, c2 in zip(s, t):
            if c1 not in mapping1:
                mapping1[c1] = c2
            elif mapping1[c1] != c2:
                return False
            if c2 not in mapping2:
                mapping2[c2] = c1
            elif mapping2[c2] != c1:
                return False
        return True

        '''
        2/2 One-liner.
        Get a set of s-t pairs, and compare its length with the s' set length and t's set length.
        '''
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))