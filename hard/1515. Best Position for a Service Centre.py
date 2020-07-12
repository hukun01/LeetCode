# 1515. Best Position for a Service Centre
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        '''
        1/2 Zoom in.
        In the 100x100 grid, first find the best 10x10 grid, and 
        keep this process until reaching the ideal precision.
        '''
        left = 100
        bottom = 100
        right = 0
        top = 0
        for x, y in positions:
            left = min(left, x)
            bottom = min(bottom, y)
            right = max(right, x)
            top = max(top, y)
        ans = math.inf
        ans_x = ans_y = 0
        delta = 100
        total_dist = lambda x1, y1: sum(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                                       for x2, y2 in positions)

        while (delta := delta / 10) >= 0.00001:
            x = left - delta
            while (x := x + delta) <= right:
                y = bottom - delta
                while (y := y + delta) <= top:
                    d = total_dist(x, y)
                    if ans > d:
                        ans = d
                        ans_x = x
                        ans_y = y
            left = ans_x - delta
            bottom = ans_y - delta
            right = ans_x + delta
            top = ans_y + delta
        return ans
        '''
        2/2 Grid search.
        Abitrarily set a starting point, here it's (0, 0), try moving it
        to 4 directions, with step size being the max range of the board,
        and keep decreasing step size as we get smaller(optimized) distances.
        Keep this process going until step size is smaller than the
        precision-based tolerance.
        '''
        total_dist = lambda x1, y1: sum(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                                       for x2, y2 in positions)
        eps = 1e-6
        x = y = 0
        total = total_dist(x, y)
        step_size = 100.0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while step_size > eps:
            found = 0
            for step_x, step_y in dirs:
                new_x = step_size * step_x + x
                new_y = step_size * step_y + y
                new_total = total_dist(new_x, new_y)
                if new_total < total:
                    total = new_total
                    x = new_x
                    y = new_y
                    found = 1
                    break
            if not found:
                step_size = step_size / 2
        return total