# 1540. Can Convert String in K Moves
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        '''
        Count the shifts frequency for each char pair with different chars.
        Remember to handle negative shifts.
        For every needed shift, if k (including wrapped around) isn't enough,
        return False.
        '''
        if len(s) != len(t):
            return False

        needed = Counter()
        for u, v in zip(s, t):
            if u != v:
                needed[(ord(v) - ord(u)) % 26] += 1
        for need, cnt in needed.items():
            if k // 26 + (k % 26 >= need) < cnt:
                return False
        return True