class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        '''
        Array.
        A critical observation is that, either A and B both match with A[0],
        or they both match with B[0]. Otherwise matching can't be done.
        To prove this, consider A as [a, b, b], B as [c, b, b], they can't match.

        Also, A can match A[0], B can match A[0] too, so in one iteration we can check both arrays.
        '''
        def find(target):
            # countA means the number of rotations from A.
            countA = countB = 0
            for a, b in zip(A, B):
                if a != b:
                    if a == target:
                        countA += 1
                    elif b == target:
                        countB += 1
                    else:
                        return -1
                elif a != target:
                    return -1
            return min(countA, countB)

        candidates = set([find(A[0]), find(B[0])])
        candidates.discard(-1)
        return min(candidates) if candidates else -1