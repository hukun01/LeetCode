# 858. Mirror Reflection
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        '''
        Math.
        Simulation can be tricky. Instead, imagine this is a
        straight line, going through reflected rooms.
        Eventually we will always hit some corner with xp == yq,
        where both x and y are integers. Then we check x and y
        and see if they are odd/even and determine which corner it is.

        Note that the scenarios are simplified as the first wall
        we hit is always the east wall, aka, p >= q.
        '''
        g = math.gcd(p, q)
        p = (p // g) % 2
        q = (q // g) % 2
        if p and q:
            return 1
        if p:
            return 0
        return 2