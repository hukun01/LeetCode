# 939. Minimum Area Rectangle
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        '''
        1/2 Brute force, Two sum (2d version)
        Iterate through every point, at each iteration, go through all seen
        points, and check if the other 2 points are seen as well. If so, update
        ans. At the end of the iteration, add current point to seen.

        Note that we need to ensure the current area is non 0, so it's a valid
        rectangle.

        Time: O(n^2) where n is len(points)
        Space: O(n)
        '''
        seen = set()
        ans = inf
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < ans:
                        ans = area
            seen.add((x1, y1))
        return ans if ans < inf else 0
        '''
        1/2 Two sum optimized (2d version)
        For each x, collect all y's on the same x, then sort the collection by
        x. Iterate through x, for each x1, and check all y pairs, if any
        (y1, y2) is in seen with a previous x2, update ans. At the end of
        iteration, update 'seen' with current { (y1, y2): x1 }.

        Note that we may have multiple (y1, y2): x, we only keep the largest
        one (which is why we need to sort x), as both small and large x's work,
        and small x leads to a bigger rectangle.

        Time: O(n^1.5), if data is generated randomly, the number of points
              would be too small to form any rectangle in the given space, so
              it would be O(n), because no two points share the same x or y.
              In the current test cases, however, there are many rectangles,
              so the worst case is O(nx * nx * ny) where nx and ny is at most
              n^0.5, and every point is part of some rectangle.
              A trick used here is to use as key the dimension with
              bigger count, e.g., if ny > nx, we use y as the key, so it is
              the outer loop, and we have O(ny*nx*nx), where nx is smaller.
              Also note that the time complexity of sort() in the inner loop is
              dominated by that of the double loop.
        Space: O(n^1.5) in the worst case above, where nx = ny = n^0.5, in the
               last_seen_x, for each x, there can be C(ny, 2) pairs of
               (y1, y2), this is ny * (ny-1) / 2 ~= ny^2 = n, and we have nx
               being n^0.5, so overall O(n^1.5).
        '''
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        x_to_ys = defaultdict(list)
        if nx > ny:
            for x, y in points:
                x_to_ys[x].append(y)
        else:
            for x, y in points:
                x_to_ys[y].append(x)

        last_seen_x = {}
        res = inf
        for x in sorted(x_to_ys):
            ys = x_to_ys[x]
            ys.sort()
            for i in range(len(ys)):
                for j in range(i):
                    y1, y2 = ys[j], ys[i]
                    if (y1, y2) in last_seen_x:
                        res = min(res, (x - last_seen_x[y1, y2]) * abs(y2 - y1))
                    last_seen_x[y1, y2] = x
        return res if res < inf else 0