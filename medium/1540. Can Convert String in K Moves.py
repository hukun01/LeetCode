# 1540. Can Convert String in K Moves
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        '''
        Count the shifts frequency for each char pair with different chars.
        Remember to handle negative shifts.
        Only the most frequent shift determines whether we can convert, as
        that shift uses the biggest step. For example, the 1st 'a->c'
        conversion takes 2 shifts, the 2nd one takes 2 + 26 * (2-1) shifts,
        the 3rd one takes 2 + 26 * (3-1) shifts. Hence the biggest shift is
        x + 26 * (count - 1) where x is the initial diff, count is the number
        of such diffs.
        Note that 'a->c' is the same as 'b->d' in terms of the diff.

        Time: O(N) where n is the length of s.
        Space: O(1), only have 26 chars.
        '''
        if len(s) != len(t):
            return False

        c = Counter((ord(c2) - ord(c1)) % 26 for c1, c2 in zip(s, t))
        return k >= max(
            (m + 26 * (count - 1) for m, count in c.items() if m),
            default = 0)