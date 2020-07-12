# 1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        '''
        For each digit, from small to big, find its first index in num,
        there must be a digit that can be found within k as long as
        k is positive. Put that digit at front and recursively call self
        with a new num after removing this used digit, and reduced k.

        A tricky point is that the time complexity is bounded by n = len(num),
        not by k, because when k is bigger than n * (n - 1) // 2, it means
        all digit pairs in num can be swapped, just return the sorted num.
        '''
        if k <= 0:
            return num
        n = len(num)
        if k >= n*(n-1)//2: 
            return "".join(sorted(list(num)))

        # From 0 to 9, for each number, find the first index
        for i in range(10):
            ind = num.find(str(i))
            if 0 <= ind <= k:
                return str(num[ind]) + self.minInteger(num[0:ind] + num[ind+1:], k-ind)