# 986. Interval List Intersections
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        '''
        Two pointers.

        The KEY is to unify the logic and be concise. Among the two lists,
        'start' can only be the *max* of A or B's starts; 'end' can only be the
        *min* of A or B's ends.

        Another KEY is when to decide which pointer to increment, we compare
        the A and B's *ends*, see which one ends earlier. Instead of *starts*.
        This is because by comparing starts, we don't really know if the
        interval with the smaller start has ended or not.
        Comparing starts would fail at examples where an interval's start is
        smaller, but ends is bigger than 2+ other intervals in another list.
        A=[[9,20]]
        B=[[11,12],[14,15]]

        Time: O(n) where n is the total length of A and B.
        Space: O(n)
        '''
        a = b = 0
        ans = []
        while a < len(A) and b < len(B):
            start = max(A[a][0], B[b][0])
            end = min(A[a][1], B[b][1])
            if start <= end:
                ans.append([start, end])
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1

        return ans