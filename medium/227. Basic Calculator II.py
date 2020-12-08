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
        number, instead of integer division, because in Py, -2//2 = -2.

        Similar to 224. Basic Calculator.

        Time: O(n) where n is the numer of chars in str s.
        Space: O(n).
        '''
        stack = []
        num = 0
        last_sign = '+'
        for c in s + '$':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-*/$':
                if last_sign == '+':
                    stack.append(num)
                elif last_sign == '-':
                    stack.append(-num)
                elif last_sign == '*':
                    stack.append(stack.pop() * num)
                elif last_sign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                last_sign = c

        return sum(stack)
        '''
        2/2 Constant space.
        Instead of using a stack, let 'prev' be the previously evaluated expression.
        If last_sign is + or -, add 'prev' to answer, and replace it with 'curr';
        If last_sign is * or /, we need to evaluate with 'curr' and update 'prev'.
        At the end, we need to add 'prev' to answer.
        Time: O(n) 
        Space: O(1)
        '''
        ans = curr = prev = 0
        last_sign = '+'
        for c in s + '$':
            if c.isdigit():
                curr = curr * 10 + int(c)

            if c in '+-*/$':
                if last_sign in '+-':
                    ans += prev
                    prev = curr if last_sign == '+' else -curr
                if last_sign == '*':
                    prev *= curr
                if last_sign == '/':
                    prev = int(prev / curr)
                last_sign = c
                curr = 0
        ans += prev
        return ans