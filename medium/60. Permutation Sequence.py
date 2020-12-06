# 60. Permutation Sequence
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''
        The total number of permutations with n-length is n!.

        We get the k-th permutation by its position, and determine its first
        digit, then the second digit, etc.

        The first digit can be found by k // fact, in which fact is (n-1)!.

        Note that after we take the nums[idx], we need to remove it.

        Time: O(n^2) because nums.pop() takes O(n) time
        Space: o(n)
        '''
        nums = list(range(1, n + 1))
        fact = factorial(nums[-1])
        ans = []
        k -= 1
        for i in range(n):
            fact //= (n - i)
            idx = k // fact
            ans.append(str(nums.pop(idx)))
            k %= fact
        return ''.join(ans)