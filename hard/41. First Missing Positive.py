# 41. First Missing Positive
class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        '''
        The answer's range would be [1, n + 1] where n is the input length.
        Put each positive number in its correct position, if a number is i,
        its position should be (i - 1).
        Be careful when swapping, avoid inline swap because a wrong order
        can become a bug.
        '''
        n = len(A)
        for i in range(n):
            while 0 <= A[i] - 1 < n and A[A[i] - 1] != A[i]:
                cached = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = cached

        return next((i + 1 for i in range(n) if i + 1 != A[i]), n + 1)