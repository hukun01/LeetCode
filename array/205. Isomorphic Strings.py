class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        Get a set of s-t pairs, and compare its length with the s' set length and t's set length.
        '''
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))