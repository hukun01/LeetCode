# 772. Basic Calculator III
class Solution:
    def calculate(self, s: str) -> int:
        '''
        Stack.
        General process is a combination of below two:
            224. Basic Calculator
            227. Basic Calculator II

        Time: O(n) where n is the numer of chars in str s.
        Space: O(n).
        '''
        stack = []
        last_sign = '+'
        num = 0
        for c in s + '$':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                stack.append(last_sign)
                stack.append('(')
                last_sign = '+'
            elif c in '+-*/)$':
                if last_sign == '+':
                    stack.append(num)
                elif last_sign == '-':
                    stack.append(-num)
                elif last_sign == '*':
                    stack.append(stack.pop() * num)
                elif last_sign == '/':
                    stack.append(int(stack.pop() / num))

                num = 0
                if c == ')':
                    while (val := stack.pop()) != '(':
                        num += val
                    last_sign = stack.pop()
                else:
                    last_sign = c

        return sum(stack)