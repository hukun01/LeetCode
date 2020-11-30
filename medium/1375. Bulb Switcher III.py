# 1375. Bulb Switcher III
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        '''
        Array.
        Note that all bulbs in light are different, meaning that
        if at moment t, the rightmost bulb is (t+1)th bulb, then
        all bulbs in [1, t+1] are on.

        Time: O(n) where n is the number of bulbs.
        Space: O(1)
        '''
        ans = right = 0
        for i, bulb in enumerate(light):
            right = max(right, bulb)
            if i + 1 == right:
                ans += 1
        return ans