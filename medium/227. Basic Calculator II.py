# 227. Basic Calculator II
class Solution:
    def calculate(self, s: str) -> int:
        '''
        1/2 Stack.
        When we see +-, we push the number with symbol to stack, because
        there may be higher priority operaters after +-.
        When we see */, we must process the num at stack peek and current num,
        immediately, because */ have the highest priority.

        Note that when processing division, we want to round down the floating
        number, instead of integer division.
        Time: O(n) where n is the numer of chars in str s.
        Space: O(n).
        '''
        stack = []
        num = 0
        lastSign = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if lastSign == '+':
                    stack.append(num)
                if lastSign == '-':
                    stack.append(-num)
                if lastSign == '*':
                    stack.append(stack.pop() * num)
                if lastSign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                lastSign = c

        return sum(stack)