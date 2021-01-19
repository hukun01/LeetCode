# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        Control flow.
        From right to left in each number, multiply every pair
        of digits, and add them together.

        Time: O(l1 * l2) where l1 is len(num1), l2 is len(num2)
        Space: O(l1 + l2)
        '''
        len1, len2 = len(num1), len(num2)
        ans = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            last1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                last2 = int(num2[j])
                p1 = i + j
                p2 = p1 + 1
                ans[p2] += last1 * last2
                ans[p1] += ans[p2] // 10
                ans[p2] %= 10
        ans = ''.join(str(c) for c in ans).lstrip('0')
        return ans if ans else '0'