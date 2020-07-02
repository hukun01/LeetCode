# 1497. Check If Array Pairs Are Divisible by k
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
        In a pair (a, b), to let (a + b) % k == 0, it must be that
        a % k + b % k == k, which is a % k == k - (b % k).
        Hence we keep track of a % k for every element a, and ensure
        that the number of (a % k) == the number of (k - (a % k)),
        we also need to handle the case when a % k == 0, need to ensure
        the number of such a is even so we can put them all in pairs.
        '''
        remainders = Counter(a % k for a in arr)
        for a in arr:
            if a % k == 0:
                if remainders[0] % 2 != 0:
                    return False
            else:
                if remainders[a % k] != remainders[k - (a % k)]:
                    return False
        return True