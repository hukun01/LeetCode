class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        The key in this problem is to write concise code.
        
        Notice that if the array starts with negatives, the left side
        and the right side will converge to the center, so we can populate
        the result array from the biggest square to the smallest one.
        
        This same logic will handle the case in which the array starts with
        positives.
        '''
        answer = [0] * len(A)
        left = 0
        right = len(A) - 1
        idx = len(A) - 1
        while left <= right:
            if abs(A[left]) < abs(A[right]):
                answer[idx] = A[right] ** 2
                right -= 1
            else:
                answer[idx] = A[left] ** 2
                left += 1
            idx -= 1
        return answer