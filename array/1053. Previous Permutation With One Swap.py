class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        '''
        From backward, find a local maximum, the first point
        where the array stops decreasing.

        From forward staring after the above local maximum,
        find the largest num that's smaller than this local maximum.
        And swap them.
        '''
        j = len(A) - 2
        while j >= 0 and A[j] <= A[j + 1]:
            j -= 1
        if j == -1:
            return A
        myI = j + 1
        for i in range(j + 1, len(A)):
            if A[i] < A[j] and A[i] > A[myI]:
                myI = i
        A[j], A[myI] = A[myI], A[j]
        return A