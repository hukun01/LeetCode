# 1497. Check If Array Pairs Are Divisible by k
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
        Two sum.

        In a pair (a, b), to let (a + b) % k == 0, it must be that
        a % k + b % k == k.
        Hence we keep track of a % k for every element a, and ensure all
        remainders[a] == remainders[k - a] for a in [1, k-1]. We need to check
        for 0 remainder separately to ensure even count of such remainders.

        Time: O(n) where n is len(arr)
        Space: O(n)
        '''
        remainders = Counter(a % k for a in arr)
        if remainders[0] % 2 != 0:
            return False
        for a in arr:
            if a % k != 0:
                if remainders[a % k] != remainders[k - (a % k)]:
                    return False
        return True