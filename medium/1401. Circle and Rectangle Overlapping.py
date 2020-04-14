# 1401. Circle and Rectangle Overlapping
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        '''
        Case by case analysis.
        First step is to translate coordination using circle center.
        In another word, treat the circle center as the origin.
        Then there are 3 cases:
        1. Circle is completely in the rectangle (distances from origin to all four vertex > radius).
        2. One vertex is in the circle (distance from origin to the closest vertex <= radius).
        3. Circle is outside of the rectangle, and no vertex is in the circle, one of the 4 edges
           contacts with the circle.
        '''
        # Coordination translation
        x1 -= x_center
        x2 -= x_center
        y1 -= y_center
        y2 -= y_center
        # Case 1
        if x1 <= 0 <= x2 and y1 <= 0 <= y2:
            return True
        def dis(x, y):
            return x**2 + y**2
        R = radius * radius
        # Case 2
        if min(dis(x1, y1), dis(x1, y2), dis(x2, y1), dis(x2, y2)) <= R:
            return True
        # Case 3
        for a, b, c in [(y1, y2, x1), (y1, y2, x2), (x1, x2, y1), (x1, x2, y2)]:
            if a <= 0 <= b and c**2 <= R:
                return True
        return False