class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = list(range(1, n + 1))
        for i in nums:
            fact *= i
        ans = []
        k -= 1
        for i in range(n):
            fact //= (n - i)
            idx = k // fact
            ans.append(str(nums.pop(idx)))
            k -= idx * fact
        return ''.join(ans)