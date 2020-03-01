class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        '''
        Iterate A twice.
        Use Lsum to denote the sum of subarray with at most L numbers,
        Lmax to denote the max Lsum we have seen so far.
        Use Msum and Mmax for similar purposes.
        
        In the first iteration, we keep L at left, M at right, so we keep adding to Msum,
        and keep sliding the M window and poping out the left side of M.
        In the meantime, when we exceed M numbers, we can start adding those
        to Lsum, and keep poping out the left side of L once we exceed L + M.
        We keep updating the Lmax, and Lmax + Msum is a candidate for the answer.
        
        In the second iteration, the logic is similar, but we keep M at left, L at right.
        '''
        ans = Lsum = Lmax = Msum = Mmax = 0
        for i in range(len(A)):
            Msum += A[i]
            if i - M >= 0:
                Msum -= A[i - M]
                Lsum += A[i - M]
            if i - L - M >= 0:
                Lsum -= A[i - L - M]
            Lmax = max(Lmax, Lsum)
            ans = max(ans, Msum + Lmax)
            
        Lsum = Lmax = Msum = Mmax = 0
        for i in range(len(A)):
            Lsum += A[i]
            if i - L >= 0:
                Lsum -= A[i - L]
                Msum += A[i - L]
            if i - L - M >= 0:
                Msum -= A[i - L - M]
            Mmax = max(Mmax, Msum)
            ans = max(ans, Lsum + Mmax)
        return ans