# 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        '''
        Greedy + Math.
        We try to subtract the largest possible fibonacci number from k,
        repeatedly, because there's no benefit in skipping it.

        For problems that find the *number* of elements that sum up to X,
        we can use division as a repeated subtraction.

        Time: O(log(k)) we at most need to use all fibonacci numbers.
        Space: O(log(k)) we need to store this many fibonacci numbers.
        '''
        f = [1, 1]
        while f[-1] < k:
            f.append(f[-1] + f[-2])
        count, end = 0, len(f) - 1
        while k > 0:
            count += k // f[end]
            k %= f[end]
            end -= 1

        return count