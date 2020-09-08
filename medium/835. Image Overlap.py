# 835. Image Overlap
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        '''
        Array.
        Naive scanning and matching doesn't do well with sparse matrix.
        Record all the 1 positions from A and B, and count their
        relative coordinates. If two pairs of points in A and B have the
        same relative coordinates, then those two pair of points will overlap
        if A is moved with the relative coordinates steps.
        Hence, the answer is the largest frequency.
        '''
        A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]
        count = Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)
        return max(count.values(), default=0)