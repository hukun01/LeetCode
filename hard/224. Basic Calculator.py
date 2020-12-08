# 224. Basic Calculator
class Solution:
    def calculate(self, s: str) -> int:
        '''
        Stack.

        Use a stack to only track positive and negative numbers and '('.
        When seeing '(', add the last sign and '(', and reset last sign.
        When seeing number, add it or its negative value based on last sign.
        When seeing ')', we need to pop out every number until we hit '('.

        Also, we append a special char '$' to end of 's', just to make tail
        handling cleaner. Without treating the last char specially, we can miss
        adding the last number if it ends with the expression, like "1 + 3".

        Finally, the stack has all flatten numbers with signs in values, we
        just need to sum it.

        Time: O(n) where n is the numer of chars in str s.
        Space: O(n)
        '''
        stack = []
        last_sign = '+'
        num = 0
        for c in s + '$':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '(':
                stack.append(last_sign)
                stack.append('(')
                last_sign = '+'
            elif c in '+-)$':
                if last_sign == '+':
                    stack.append(num)
                elif last_sign == '-':
                    stack.append(-num)
                if c == ')':
                    num = 0
                    while (val := stack.pop()) != '(':
                        num += val
                    last_sign = stack.pop()
                    # the next iteration we will come back to this branch, so
                    # reuse it to process the updated num and last_sign.
                else:
                    num = 0
                    last_sign = c

        return sum(stack)