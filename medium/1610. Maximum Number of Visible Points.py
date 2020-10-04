# 1610. Maximum Number of Visible Points
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        '''
        Computation geometry + sliding window + cycle array.
        '''
        def get_angle(y, x):
            a = math.degrees(math.atan2(y, x))
            return (a + 360) % 360
        maps = Counter()
        l_x, l_y = location
        same = 0
        for i, (x, y) in enumerate(points):
            if (x, y) == (l_x, l_y):
                same += 1
                continue
            a = get_angle(y - l_y, x - l_x)
            maps[a] += 1
        all_angles = sorted(maps.keys())
        # A key is the cover the cycle scenario, like from 350 to 80, if the angle is 90.
        for key, count in list(maps.items()):
            maps[key + 360] = count
        all_angles = all_angles + [key + 360 for key in all_angles]

        left = 0
        count = ans = 0
        for i, a in enumerate(all_angles):
            count += maps[a]
            while left < i and a - all_angles[left] > angle:
                count -= maps[all_angles[left]]
                left += 1
            ans = max(ans, count)
        return ans + same