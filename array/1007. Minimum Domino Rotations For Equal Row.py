class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        '''
        A critical observation is that, either A and B both match with A[0],
        or they both match with B[0]. Otherwise matching can't be done.
        To prove this, consider A as [a, b, b], B as [c, b, b], they can't match.
        '''
        
        def shapeMatchingRotations(shape1, shape2):
            count1 = count2 = 0
            for a1, a2 in zip(shape1, shape2):
                if a1 != a2:
                    if a1 == shape1[0]:
                        count1 += 1
                    elif a2 == shape1[0]:
                        count2 += 1
                    else:
                        return -1
                elif a1 != shape1[0]:
                    return -1
            return min(count1, count2)
        
        r1 = shapeMatchingRotations(A, B)
        r2 = shapeMatchingRotations(B, A)
        if r1 != -1 and r2 != -1:
            return min(r1, r2)
        else:
            return max(r1, r2)