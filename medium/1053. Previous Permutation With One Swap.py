class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        '''
        From backward, find a local maximum, the first point
        where the array starts increasing. Let j be its index.

        From forward staring after the above local maximum, find the largest
        num that's smaller than this local maximum. Let k be its index.
        Swap A[j] and A[k].

        As long as we can find a good j, we can always find "the largest
        permutation smaller than arr", with one swap. But note that this may
        not be the actual largest permutation smaller than arr, this is just
        the one that can be achieved by one swap.

        Time: O(n) where n is len(A)
        Space: O(1)
        '''
        j = len(A) - 2
        while 0 <= j and A[j] <= A[j + 1]:
            j -= 1
        if j == -1:
            return A
        k = j + 1
        for i in range(j + 1, len(A)):
            if A[k] < A[i] < A[j]:
                k = i
        A[j], A[k] = A[k], A[j]
        return A