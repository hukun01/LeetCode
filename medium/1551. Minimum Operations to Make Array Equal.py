# 1551. Minimum Operations to Make Array Equal
class Solution:
    def minOperations(self, n: int) -> int:
        '''
        Math.
        This is an arithmetic sequence of odd numbers with common difference
        as 2.
        Target is n, which is also the average number in array.
        We only need to count the differences between target and the first
        half of the numbers smaller than target.
        The total of an arithmetic sequence is (a0 + ax) * count // 2

        Time: O(1)
        Space: O(1)
        '''
        target = n
        count = n // 2
        delta = -2
        a0 = target - 1
        ax = a0 + delta * (count - 1)
        return (a0 + ax) * count // 2