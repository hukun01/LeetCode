# 149. Max Points on a Line
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        1/2 Math and hashmap.
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
            b = x1 - x2, then we know
            c = x1*(y1 - y2) + y1*(x2 - x1) = x2*y1 - x1*y2
        Note that (a, b, c) is equivalent to (-a, -b, -c), so we ensure 'a' is
        always positive, by flipping (a, b, c) when 'a' is negative.
        Also note that (5, 15, 25) is equivalent to (1, 3, 5), so we need to
        find the gcd() among (a, b, c) and use the smallest possible numbers to
        represent the line.

        Two edge cases:
        1. when x1 == x2 and y1 == y2, we can't calculate gcd(a, b, c) as it
           would be g(0, 0, c) and we can't have 2 zeros. Hence, we need to
           set the line with (a, b, c) being (1, 0, -x1).
        2. when there's no lines found (due to 0 points, or all points being
           the same), line_to_points would be empty, we need to return the
           len(points) as result.

        Time: O(n^2)
        Space: O(n^2)
        '''
        line_to_points = defaultdict(set)
        n = len(points)
        for i1 in range(n):
            x1, y1 = points[i1]
            for i2 in range(i1+1, n):
                x2, y2 = points[i2]
                if x1 == x2 and y1 == y2:
                    a = 1
                    b = 0
                    c = -x1
                else:
                    a = y2 - y1
                    b = x1 - x2
                    c = x2 * y1 - x1 * y2
                    if a < 0:
                        a, b, c = -a, -b, -c
                    g = gcd(a, b, c)
                    a, b, c = a/g, b/g, c/g
                line = (a, b, c)
                line_to_points[line].add(i1)
                line_to_points[line].add(i2)

        return max((len(v) for v in line_to_points.values()), default = len(points))
        '''
        2/2 Deduplicate points before processing.
        Optimized space and reduce the first edge case.
        '''
        points = Counter([tuple(p) for p in points])
        n = len(points)
        if n <= 1:
            return max(points.values(), default = 0)
        line_to_points = defaultdict(set)

        for (x1, y1), (x2, y2) in combinations(points, 2):
            a = y2 - y1
            b = x1 - x2
            c = x2 * y1 - x1 * y2
            if a < 0:
                a, b, c = -a, -b, -c
            g = gcd(a, b, c)
            a, b, c = a/g, b/g, c/g
            line = (a, b, c)
            line_to_points[line].add((x1, y1))
            line_to_points[line].add((x2, y2))

        return max(sum(points[p] for p in v) for v in line_to_points.values())