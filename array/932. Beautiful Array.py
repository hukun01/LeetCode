class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        
        Note that these 3 operations won't change the beauty of an array.
        Given A[k] * 2 != A[i] + A[j],
        1. Addition to every element: (A[k] + x) * 2 != (A[i] + x) + (A[j] + x)
        2. Deletion: same as addition
        3. Multiplication: A[k] * 2 != A[i] + A[j], so (A[k] * x) * 2 != (A[i] * x) + (A[j] * x)

        With the observations above, we can easily construct any beautiful array.
        Assume we have a beautiful array A with length N

        A1 = A * 2 - 1 is beautiful with only odds from 1 to N * 2 -1
        A2 = A * 2 is beautiful with only even from 2 to N * 2
        B = A1 + A2 beautiful array with length N * 2
        """
        A = [1]
        while len(A) < N:
            A = [2 * a - 1 for a in A] + [2 * a for a in A]
        return [a for a in A if a <= N]