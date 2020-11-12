# 593. Valid Square
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
        Geometry.
        Sort the 4 points and we will find the edges and diagnols, check
        if they are the same.
        '''
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        dist = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        edge_equal = dist(p1, p2) == dist(p1, p3) == dist(p2, p4) == dist(p3, p4) != 0
        diagnol_equal = dist(p1, p4) == dist(p2, p3)
        return edge_equal and diagnol_equal