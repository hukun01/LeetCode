# 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Greedy.
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