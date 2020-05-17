# 1453. Maximum Number of Darts Inside of a Circular Dartboard
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        '''
        Computational geometry.
        Angular sweep.

        Fundamentals:
        Thales's theorem: if A, B, and C are distinct points on a circle
        where the line AC is a diameter, then the angle ∠ABC is a right angle.
        Trigonometric (triangle) functions: atan2 and acos returns the angles
        given the ratio of corresponding edges.

        Pick a point pair P-Q, given the radius, there are at most 2 circles, so
        that the two points are *on* the circles. Then we have a range of angles,
        within which the circle will cover both points. Given one point P, we find
        all the Qs and angle ranges, and recode the entry and exit, then sort the
        angle pairs. Now we go through all angle pairs for P-{all Q}, and find the
        max number of entries. Note that for the same angle, we want to count the entry
        first, so we flip the entry/exit during sort.
        Repeat this for all point P, we will find the answer.
        '''
        ans = 1
        for x, y in points:
            angles = []
            for x1, y1 in points:
                # the other point is Q
                if (x, y) != (x1, y1) and (d := sqrt((x1-x)**2 + (y1-y)**2)) <= 2*r:
				    # angle between line P-Q and the positive x axis.
                    angle = atan2(y1 - y, x1 - x)
                    delta = acos(d / (2*r))
                    angles.append((angle - delta, 1)) # entry
                    angles.append((angle + delta, -1)) # exit
            angles.sort(key = lambda x: (x[0], -x[1]))
            val = 1
            print(angles)
            for _, entry in angles:
                ans = max(ans, val := val + entry)
        return ans