class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            nums.append(i)
        l = k - 1

        ans = []
        for i in range(n):
            factorial //= (n - i)
            idx = l // factorial
            ans.append(str(nums.pop(idx)))
            l -= idx * factorial
        return "".join(ans)