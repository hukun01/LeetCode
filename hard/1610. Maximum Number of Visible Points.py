# 1610. Maximum Number of Visible Points
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        '''
        Computation geometry + sliding window + cycle array.
        '''
        location = tuple(location)
        def get_angle(y, x):
            a = math.degrees(math.atan2(y - location[1], x - location[0]))
            return (a + 360) % 360
        
        degrees = [get_angle(y, x) for i, (x, y) in enumerate(points) if (x, y) != location]
        same = len(points) - len(degrees)
        degrees.sort()
        degrees += [d + 360 for d in degrees]
        # A key is the cover the cycle scenario, like from 350 to 80, if the angle is 90.
        left = 0
        ans = 0
        for i, a in enumerate(degrees):
            while left < i and a - degrees[left] > angle:
                left += 1
            ans = max(ans, i - left + 1)
        return ans + same