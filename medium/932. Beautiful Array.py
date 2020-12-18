class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        """
        Odd + Even parts makes a beautiful array!

        Note that these 3 operations won't change the beauty of an array.
        Given A[k] * 2 != A[i] + A[j],
        1. Addition to every element: (A[k] + x) * 2 != (A[i] + x) + (A[j] + x)
        2. Deletion: same as addition
        3. Multiplication: (A[k] * x) * 2 != (A[i] * x) + (A[j] * x)

        Another key is to concat two beautiful arrays, if we have below:
            A1 = A * 2 - 1 is beautiful with only [odds] from 1 to N * 2 - 1
            A2 = A * 2 is beautiful with only [even] from 2 to N * 2
        Then: B = A1 + A2 is a beautiful array with length N * 2
        This works because A1 and A2 by themselves are already beautiful, and
        when they merge, any i,j,k from the middle part can't break the rule,
        because B[i] + B[j] is odd.

        Finally, the process is to
        1. start from a simple beautiful array [1];
        2. apply above update operations to make an odd value array A1 and an
           even value array A2 from #1;
        3. concat A1 and A2 to make a bigger beautiful array;
        4. Once we exceed N, we take the first N elements <= N, as it's ok to
           skip bigger elements without breaking the beauty of the array.
        """
        A = [1]
        while len(A) < N:
            A = [2 * a - 1 for a in A] + [2 * a for a in A]
        return [a for a in A if a <= N]