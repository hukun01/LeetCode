# 149. Max Points on a Line
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        Math and hashmap.
        A straightforward way is to try every point pair that forms a line,
        and collect all line to points mapping, and find the line with most
        points. The trick here is to deal with floating point precision. We
        can't represent a line with (a, b) from 'y = ax + b', because a may be
        a floating point, and thus suffers from inaccurate comparsion. For
        example, when seeing 0.00000009 = 0.00000009, we aren't sure if they
        are the same, because they may actually be 0.000000089 and 0.000000088.
        We need another way to represent lines.
        Let a line be 'ax + by + c = 0', we can use (a, b, c) to represent the
        line. With two points on the line, we have
            a*x1 + b*y1 + c = 0, and 
            a*x2 + b*y2 + c = 0, then we have
            a*x1 + b*y1 = a*x2 + b*y2, hence
            a*(x1 - x2) = b*(y2 - y1), so we know
            a = y2 - y1
            b = x1 - x2

        We can fix one point, and traverse the next set of points. This way,
        we only need to collect the slopes (a, b), but not the intercept (c).

        One edge case is that when (x1 - x2) == 0, we need to track the
        abs(y1 - y2), so the gcd would be abs(y1 - y2), and the slope would be
        (0, 1).

        Time: O(n^2)
        Space: O(n)
        '''
        if len(points) < 2:
            return len(points)

        def slope(i, j):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            if dx < 0:
                dx, dy = -dx, -dy
            if dx == 0:
                dy = abs(dy)
            g = gcd(dx, dy)
            return dx // g, dy // g

        n = len(points)
        max_points = 2

        for i in range(n - 1):
            slope_counter = Counter(slope(i, j) for j in range(i + 1, n))
            max_points = max(max_points, max(slope_counter.values()) + 1)

        return max_points