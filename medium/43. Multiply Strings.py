# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        Control flow.
        From right to left in each number, multiply every pair
        of digits, and add them together.

        Note about edge case '0' * '0' where answer is '0'; and '9' * '9',
        where answer has carryover being 8, while typical carryover is 1.

        Time: O(l1 * l2) where l1 is len(num1), l2 is len(num2)
        Space: O(l1 + l2)
        '''
        n1 = len(num1)
        n2 = len(num2)
        ans = [0] * (n1 + n2)
        for i, a in enumerate(reversed(num1)):
            for j, b in enumerate(reversed(num2)):
                val = int(a) * int(b)
                ans[i+j] += val
                carry = ans[i+j] // 10
                ans[i+j] %= 10
                if carry > 0:
                    ans[i+j+1] += carry

        return ''.join(str(c) for c in reversed(ans)).lstrip('0') or '0'