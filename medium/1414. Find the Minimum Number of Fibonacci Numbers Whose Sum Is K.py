# 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        '''
        For problems that find the *number* of elements that sum up to X,
        we can use division as a repeated subtraction.
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