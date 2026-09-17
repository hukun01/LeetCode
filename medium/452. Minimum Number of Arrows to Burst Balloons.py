# 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        1/2 Greedy.
        Similar to 252. Meeting Rooms, we sort the points by their ends.
        Then we group points whose starts are less than the previous end,
        the ends are increasing (as we sort), so the later point only ends
        later, but if it starts earlier than some previous point, then we
        can shoot them with one arrow.
        We only need a new arrow when the current point starts after the
        previous end.
        '''
        ans = 0
        prev_e = -math.inf
        for s, e in sorted(points, key=lambda p: p[1]):
            if s > prev_e:
                ans += 1
                prev_e = e
        return ans


        '''
        2/2 Scanning line.
        
        We want to find out the min number of intervals, scan them with a vertical line.
        
        We maintain a scanning area, and check the next point and 
        determine if it falls into this scanning area. 
        A point falls into the area when it overlaps with it (aka, its start is in the area).
        When a point falls out, we start a new area for it.
        Each area needs 1 arrow.

        The area is determined by the largest starts and the smallest ends we have seen.
        area_s = max(s, area_s)
        area_e = min(e, area_e)

        Initialize the area with the first point.
        '''
        points.sort(key=lambda x: x[0])
        ans = 1
        area_s, area_e = points[0][0], points[0][1]
        for s, e in points:
            if area_s <= s <= area_e:
                area_s = max(s, area_s)
                area_e = min(e, area_e)
            else:
                ans += 1
                area_s, area_e = s, e
        
        return ans
