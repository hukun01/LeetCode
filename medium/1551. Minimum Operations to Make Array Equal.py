# 1551. Minimum Operations to Make Array Equal
class Solution:
    def minOperations(self, n: int) -> int:
        '''
        Math.
        Assuming the array is arr.
        If n is odd, we need to balance arr[0] and arr[-1] for (n-1) times,
        arr[1] and arr[-2] for (n-3) times, ... 
        arr[(n-1)/2-1] and arr[(n+1)/2] for 2 times.
        Total is (n-1)/2 * (2 + n - 1)/2 = n//2 * (n//2 + 1)

        If n is even, we need to balance arr[0] and arr[-1] for (n-1) times,
        arr[1] and arr[-2] for (n-3) times, ... 
        arr[(n-1)/2] and arr[n/2] for 1 times.
        Total is (n/2) * (1 + n - 1)/2 = n//2 * n//2
        '''
        count = n // 2
        return count * (count + n % 2)